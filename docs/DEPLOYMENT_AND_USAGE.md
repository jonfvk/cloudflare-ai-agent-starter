# Deployment and Usage Guide

This document provides step-by-step instructions to deploy and use the Cloudflare AI Agent Starter Kit.

---

## Prerequisites

- A Cloudflare account with Workers and Durable Objects enabled.
- Cloudflare CLI (`wrangler`) installed and configured.
- Basic knowledge of JavaScript/TypeScript and Python for understanding the starter kit.

---

## Deployment Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd cloudflare-ai-agent-starter
   ```

2. **Configure Wrangler**

   - Ensure your `wrangler.toml` is set up with your Cloudflare account ID and project details.
   - Define Durable Objects and KV namespaces as needed.

3. **Build the project**

   Since this starter kit is Python-simulated code, adapt or transpile as needed for your Worker environment.

4. **Publish to Cloudflare Workers**

   Use the Wrangler CLI:

   ```bash
   wrangler publish
   ```

   This deploys your Worker globally on Cloudflare's edge network.

5. **Verify deployment**

   Access the deployed Worker URL (provided by Wrangler) in your browser.

---

## Usage Instructions

### Web Frontend

- Open the Worker URL in a modern web browser.
- You will see a simple chat interface.
- Type a message in the input box and press **Send** or hit **Enter**.
- The AI agent will respond based on the conversation history.

### API Gateway

- The Worker exposes an API endpoint at `/api/agent`.
- Send a POST request with JSON body `{ "message": "your message" }`.
- The response JSON will contain the AI agent's reply.

Example using `curl`:

```bash
curl -X POST https://<your-worker-url>/api/agent \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello AI!"}'
```

Expected response:

```json
{
  "status": "ok",
  "reply": "Simulated response to: 'User: Hello AI!' using model gpt-4o."
}
```

---

## Notes

- This starter kit simulates AI responses and Durable Object state locally.
- For production, integrate with actual Cloudflare Workers AI APIs and Durable Objects.
- The KV storage is simulated; configure real Workers KV namespaces for persistence.

---

## References

- Cloudflare Workers AI: https://developers.cloudflare.com/workers/runtime-apis/ai/
- Durable Objects: https://developers.cloudflare.com/workers/learning/using-durable-objects/
- Workers KV: https://developers.cloudflare.com/workers/runtime-apis/kv/

---

## Source

- https://www.cloudflare.com/press/press-releases/2026/more-than-10-million-developers-are-building-on-cloudflare (2026-06)
