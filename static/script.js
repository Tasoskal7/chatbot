async function sendMessage() {
    const userInput = document.getElementById('userInput').value.trim();
    if (!userInput) return;

    const messages = document.getElementById('messages');
    messages.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput }),
        });

        const data = await response.json();
        messages.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
    } catch (error) {
        messages.innerHTML += `<div><strong>Bot:</strong> Error connecting to server.</div>`;
    }

    document.getElementById('userInput').value = '';
    messages.scrollTop = messages.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
