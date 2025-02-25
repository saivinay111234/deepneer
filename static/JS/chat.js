document.addEventListener("DOMContentLoaded", function() {
    loadChatMessages();
});

function loadChatMessages() {
    fetch(window.location.pathname + "/chat")
        .then(response => response.json())
        .then(data => {
            const chatMessages = document.getElementById("chat-messages");
            chatMessages.innerHTML = "";
            data.messages.forEach(msg => {
                const li = document.createElement("li");
                li.textContent = `${msg.username}: ${msg.message}`;
                chatMessages.appendChild(li);
            });
        });
}

function sendMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (!message) return;

    fetch(window.location.pathname + "/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: "Anonymous", message: message })
    }).then(() => {
        input.value = "";
        loadChatMessages();
    });
}
