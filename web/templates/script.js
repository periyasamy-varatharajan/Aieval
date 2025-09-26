async function sendMessage() {
  const input = document.getElementById("userInput");
  const msg = input.value.trim();
  if (!msg) return;

  appendMessage("user", msg);
  input.value = "";

  try {
    const res = await fetch("/api/chat/send", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    appendMessage("bot", data.reply || "No response");
  } catch (err) {
    appendMessage("bot", "⚠️ Error connecting to server");
  }
}

function appendMessage(role, text) {
  const msgDiv = document.createElement("div");
  msgDiv.className = `message ${role}`;
  msgDiv.innerText = text;

  const messages = document.getElementById("messages");
  messages.appendChild(msgDiv);
  messages.scrollTop = messages.scrollHeight;
}
