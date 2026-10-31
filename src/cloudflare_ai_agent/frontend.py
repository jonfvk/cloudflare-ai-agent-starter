def render_html_page():
    """Return a simple HTML page string for interacting with the AI agent."""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cloudflare AI Agent</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2em; background: #f9f9f9; }
        h1 { color: #333; }
        #chat { border: 1px solid #ccc; padding: 1em; height: 300px; overflow-y: auto; background: #fff; }
        .message { margin: 0.5em 0; }
        .user { color: #007acc; }
        .agent { color: #d14; }
        #input-area { margin-top: 1em; }
        #user-input { width: 80%; padding: 0.5em; font-size: 1em; }
        #send-btn { padding: 0.5em 1em; font-size: 1em; }
    </style>
</head>
<body>
    <h1>Cloudflare AI Agent</h1>
    <div id="chat"></div>
    <div id="input-area">
        <input type="text" id="user-input" placeholder="Type your message here..." />
        <button id="send-btn">Send</button>
    </div>

    <script>
        const chat = document.getElementById('chat');
        const userInput = document.getElementById('user-input');
        const sendBtn = document.getElementById('send-btn');

        function appendMessage(role, text) {
            const div = document.createElement('div');
            div.className = 'message ' + role;
            div.textContent = (role === 'user' ? 'You: ' : 'Agent: ') + text;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }

        async function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;
            appendMessage('user', message);
            userInput.value = '';

            try {
                const response = await fetch('/api/agent', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message })
                });
                if (!response.ok) {
                    appendMessage('agent', 'Error: ' + response.statusText);
                    return;
                }
                const data = await response.json();
                if (data.status === 'ok' && data.reply) {
                    appendMessage('agent', data.reply);
                } else {
                    appendMessage('agent', 'Error: Invalid response from agent.');
                }
            } catch (err) {
                appendMessage('agent', 'Error: ' + err.message);
            }
        }

        sendBtn.addEventListener('click', sendMessage);
        userInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
"""
    return html
