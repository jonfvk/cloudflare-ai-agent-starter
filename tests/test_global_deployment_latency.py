import unittest
import time
from src.cloudflare_ai_agent.api_gateway import APIGateway
from src.cloudflare_ai_agent.durable_object import DurableObject

class TestGlobalDeploymentLatency(unittest.TestCase):
    """Test global deployment and latency simulation."""

    def setUp(self):
        # Simulate storage for Durable Object
        self.storage = {}
        self.api_gateway = APIGateway(self.storage)

    def test_latency_and_response(self):
        # Initialize Durable Object
        import asyncio
        asyncio.run(self.api_gateway.durable_object.initialize())

        # Simulate sending a message and measure latency
        request = {
            'path': '/api/agent',
            'method': 'POST',
            'body': {'message': 'Hello from test!'}
        }

        start_time = time.perf_counter()
        response = asyncio.run(self.api_gateway.handle_api_request(request))
        end_time = time.perf_counter()

        latency_ms = (end_time - start_time) * 1000

        # Check response structure
        self.assertIn('status', response)
        self.assertEqual(response['status'], 'ok')
        self.assertIn('reply', response)
        self.assertIsInstance(response['reply'], str)

        # Check latency is within reasonable bounds (simulated environment)
        # Since this is local simulation, expect < 100ms
        self.assertLess(latency_ms, 100, f"Latency too high: {latency_ms} ms")

    def test_multiple_messages_latency(self):
        import asyncio
        asyncio.run(self.api_gateway.durable_object.initialize())

        messages = ["Hello", "How are you?", "Tell me a joke."]

        for msg in messages:
            request = {
                'path': '/api/agent',
                'method': 'POST',
                'body': {'message': msg}
            }
            start_time = time.perf_counter()
            response = asyncio.run(self.api_gateway.handle_api_request(request))
            end_time = time.perf_counter()

            latency_ms = (end_time - start_time) * 1000

            self.assertEqual(response.get('status'), 'ok')
            self.assertIn('reply', response)
            self.assertLess(latency_ms, 100, f"Latency too high for message '{msg}': {latency_ms} ms")

if __name__ == '__main__':
    unittest.main()
