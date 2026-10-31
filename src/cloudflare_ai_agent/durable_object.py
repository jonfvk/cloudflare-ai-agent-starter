import json
from typing import Dict

class SessionState:
    """Class to hold session state data."""

    def __init__(self):
        self.history = []  # List of messages exchanged in the session

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def to_json(self) -> str:
        return json.dumps({"history": self.history})

    @staticmethod
    def from_json(data: str):
        obj = SessionState()
        try:
            parsed = json.loads(data)
            obj.history = parsed.get("history", [])
        except Exception:
            obj.history = []
        return obj

class DurableObject:
    """Simulated Durable Object for session state management."""

    def __init__(self, state_storage: Dict[str, str]):
        # state_storage simulates persistent storage for this Durable Object instance
        self.state_storage = state_storage
        self.state_key = "session_state"
        self.session_state = None

    async def initialize(self):
        # Load existing state or initialize new
        data = self.state_storage.get(self.state_key)
        if data:
            self.session_state = SessionState.from_json(data)
        else:
            self.session_state = SessionState()

    async def handle_request(self, request: Dict) -> Dict:
        """
        Handle a request to the Durable Object.

        Args:
            request (Dict): A dict with keys 'action' and optionally 'message'.

        Returns:
            Dict: Response dict with updated session history or error.
        """
        action = request.get("action")

        if action == "add_message":
            role = request.get("role", "user")
            content = request.get("message", "")
            self.session_state.add_message(role, content)
            # Persist state
            self.state_storage[self.state_key] = self.session_state.to_json()
            return {"status": "ok", "history": self.session_state.history}

        elif action == "get_history":
            return {"status": "ok", "history": self.session_state.history}

        else:
            return {"status": "error", "message": "Unknown action."}
