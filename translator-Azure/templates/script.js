const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const userText = input.value.trim();
  if (!userText) return;

  addMessage(userText, 'user');

  // Enviar mensagem ao back-end Python
  try {
    const response = await fetch("http://localhost:5000/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: userText })
    });
    const data = await response.json();
    addMessage(data.translation, 'bot');
  } catch (error) {
    addMessage("⚠️ Erro ao conectar com o servidor.", 'bot');
  }

  input.value = '';
});

function addMessage(text, sender) {
  const div = document.createElement('div');
  div.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
  div.innerText = text;
  chatMessages.appendChild(div);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
