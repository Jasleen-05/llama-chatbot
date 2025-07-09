window.addEventListener('DOMContentLoaded', () => {
  let history = [];

  const input = document.getElementById("message");
  const chatbox = document.getElementById("chatbox");

  async function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    chatbox.innerHTML += `
  <div class="user fade-in">
    <div class="message">You: ${msg}</div>
  </div>`;
    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    try {
      const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg, history: history })
      });

      const data = await res.json();
      const botReply = data.response;

      chatbox.innerHTML += `
  <div class="bot fade-in">
    <div class="message">Bot: ${botReply}</div>
  </div>`;
      chatbox.scrollTop = chatbox.scrollHeight;

      history.push([msg, botReply]);
    } catch (error) {
      chatbox.innerHTML += `
  <div class="bot fade-in">
    <div class="message">⚠️ Error: Could not get a response.</div>
  </div>`;
    }
  }

  input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      sendMessage();
    }
  });
});