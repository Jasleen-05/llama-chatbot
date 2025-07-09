# 🤖 LLaMA Chatbot – Local AI Assistant

Welcome to **LLaMA Chatbot**, a local Flask-based conversational assistant powered by the **LLaMA model**. This chatbot runs completely offline and can respond to user prompts in a natural, human-like way.

> 🔒 No API keys needed. Fully local. Privacy-first.

---

## 🧠 Features

- ✅ Powered by a fine-tuned **LLaMA model**
- 🧩 Built with **Transformers**, **PyTorch**, and **Flask**
- 🎨 Custom frontend with responsive UI
- 🌐 Supports **local hosting** without internet
- 💬 Chat UI with instant feedback

---

## 🖥️ Demo

![Chatbot Demo Screenshot]![image](https://github.com/user-attachments/assets/b78c2244-3555-48ec-b192-16084eb18957)


---

## 📦 Folder Structure
```
llama-chatbot/
├── app1.py
├── templates/
│ └── index.html
├── static/
│ ├── styles.css
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/llama-chatbot.git
cd llama-chatbot
```
2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Make sure your fine-tuned model is in the directory
Update model_path in app.py to your correct path, e.g.:
```
model_path = "trained_model_20250708_032008"
```
5. Run the app
```
python app1.py
```
Visit: http://localhost:5005

---

⚙️ **Tech Stack**  
- Flask Backend API & Web Server  
- Transformers for model loading & text generation  
- PyTorch deep learning engine  
- HTML / CSS / JS Frontend

---

🧪 **Sample Prompt**  
**You**: What is quantum computing?  
**Bot**: Quantum computing is a type of computing that uses the principles of quantum mechanics, a branch of physics that describes the behavior of matter and energy at the smallest scales.....

---

❓ **FAQ**  
- **Q**: Can this run on CPU?  
  **A**: Yes, but slower. GPU (CUDA) is preferred for real-time response.

- **Q**: Do I need internet or Hugging Face keys?  
  **A**: No. The model is fully local. Just point `model_path` to your fine-tuned directory.

- **Q**: Can I swap the LLaMA model with another?  
  **A**: Yes! As long as it’s compatible with `AutoModelForCausalLM`.

---

📄 **License**  
MIT License – You can use, modify, and distribute it for both personal and commercial purposes.

---

✨ **Author**  
Made by **Jasleen Kaur Matharoo**  
GitHub: [@Jasleen-05](https://github.com/Jasleen-05)  
Email: [jasleen.matharoo@s.amity.edu](mailto:jasleen.matharoo@s.amity.edu)
