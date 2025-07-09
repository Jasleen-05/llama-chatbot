from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# ✅ Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# ✅ Hugging Face token from environment
HF_TOKEN = os.getenv("HF_TOKEN")

# Model ID
model_id = "meta-llama/Llama-2-7b-chat-hf"
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🖥️ Using device: {device}")

# ✅ Enable CuDNN benchmark for speed boost
torch.backends.cudnn.benchmark = True

# ✅ Quantization config for 4-bit offloading
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

# ✅ Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id, token=HF_TOKEN, use_fast=True)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    token=HF_TOKEN,
    quantization_config=bnb_config,
    device_map="auto"
)

# ✅ Optional: Compile the model (for PyTorch 2.x and CUDA only)
if hasattr(torch, 'compile'):
    model = torch.compile(model)

# ✅ Response generation function
def generate_response(user_input, history=[]):
    prompt = ""
    for user_msg, bot_msg in history:
        prompt += f"<s>[INST] {user_msg} [/INST] {bot_msg} </s>"
    prompt += f"<s>[INST] {user_input} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=800,  # Fixed value (no dynamic adjustment)
            do_sample=True,
            top_p=0.95,
            top_k=50,
            temperature=0.7
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    reply = decoded.split("[/INST]")[-1].strip()
    return reply

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data['message']
    chat_history = data.get('history', [])
    response = generate_response(user_input, chat_history)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)