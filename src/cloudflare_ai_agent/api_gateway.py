import json
from typing import Dict, Any
from src.cloudflare_ai_agent.durable_object import DurableObject
from src.cloudflare_ai_agent.worker import WorkersAIClient

class APIGateway:
    """Basic API gateway to route and handle requests."""

    def __init__(self, durable_object_storage: Dict[str, str]):
        # Initialize Durable Object with provided storage
        self.durable_object = DurableObject(durable_object_storage)

    async def initialize(self):
        await self.durable_object.initialize()

    async def handle_api_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle incoming API requests.

        Args:
            request (Dict): A dictionary representing the API request.
                Expected keys:
                  - 'path': str, the API endpoint path
                  - 'method': str, HTTP method (e.g., 'POST')
                  - 'body': Dict, parsed JSON body of the request

        Returns:
            Dict: JSON-serializable response dictionary.
        """
        path = request.get('path', '')
        method = request.get('method', 'GET').upper()
        body = request.get('body', {})

        if path == '/api/agent' and method == 'POST':
            message = body.get('message')
            if not message or not isinstance(message, str):
                return {"status": "error", "message": "Missing or invalid 'message' in request body."}

            # Add user message to session state
            add_msg_resp = await self.durable_object.handle_request({
                "action": "add_message",
                "role": "user",
                "message": message
            })
            if add_msg_resp.get("status") != "ok":
                return {"status": "error", "message": "Failed to update session state."}

            # Prepare prompt from session history
            history = add_msg_resp.get("history", [])
            prompt = self._build_prompt_from_history(history)

            # Call AI model
            ai_client = WorkersAIClient()
            ai_reply = ai_client.generate_response(prompt)

            # Add AI reply to session state
            await self.durable_object.handle_request({
                "action": "add_message",
                "role": "agent",
                "message": ai_reply
            })

            return {"status": "ok", "reply": ai_reply}

        else:
            return {"status": "error", "message": "Unknown API endpoint or method."}

    def _build_prompt_from_history(self, history) -> str:
        """Build a prompt string from the conversation history."""
        lines = []
        for entry in history:
            role = entry.get('role', 'user')
            content = entry.get('content', '')
            prefix = 'User:' if role == 'user' else 'Agent:'
            lines.append(f"{prefix} {content}")
        return '\n'.join(lines)
