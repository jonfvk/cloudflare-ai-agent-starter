import json
from typing import Optional

class WorkersKV:
    """Simulated Workers KV namespace for persistent key-value storage."""

    def __init__(self):
        self.store = {}

    async def get(self, key: str) -> Optional[str]:
        """Retrieve a value by key."""
        return self.store.get(key)

    async def put(self, key: str, value: str) -> None:
        """Store a value by key."""
        self.store[key] = value

class KVStorage:
    """Wrapper around WorkersKV to manage persistent session data."""

    def __init__(self, kv_namespace: WorkersKV):
        self.kv = kv_namespace

    async def save_session(self, session_id: str, data: dict) -> None:
        serialized = json.dumps(data)
        await self.kv.put(session_id, serialized)

    async def load_session(self, session_id: str) -> Optional[dict]:
        data = await self.kv.get(session_id)
        if data is None:
            return None
        try:
            return json.loads(data)
        except Exception:
            return None
