# Example Repository and Demo Guide

This document provides details about the example repository and demo for the Cloudflare AI Agent Starter Kit.

---

## Repository Overview

The repository contains a minimal example application demonstrating how to build and deploy a globally distributed AI-native application using Cloudflare Workers AI and Durable Objects. It includes:

- AI agent integration with simulated AI responses.
- Durable Objects for session state management.
- Workers KV simulation for persistent storage.
- A simple web frontend chat interface.
- An API gateway to handle AI agent requests.
- Logging and error handling.
- Tests for global deployment and latency.

---

## Demo

A live demo is available once you deploy the Worker using the instructions in the Deployment and Usage Guide (`docs/DEPLOYMENT_AND_USAGE.md`).

### Accessing the Demo

1. Deploy the Worker using Wrangler CLI:

   ```bash
   wrangler publish
   ```

2. Open the Worker URL provided by Wrangler in a modern web browser.

3. Interact with the AI agent via the chat interface.

4. Alternatively, send POST requests to the `/api/agent` endpoint with JSON payloads to test the API gateway.

---

## Repository Structure

- `src/cloudflare_ai_agent/` - Source code for the AI agent, Durable Objects, API gateway, frontend, and utilities.
- `docs/` - Documentation including deployment, usage, and this demo guide.
- `tests/` - Unit tests for key components.
- `README.md` - Project overview and milestones.

---

## Contributing

Contributions to improve the starter kit, add features, or enhance documentation are welcome. Please fork the repository and submit pull requests.

---

## License

This project is provided as-is for educational and demonstration purposes.

---

## Source

- https://www.cloudflare.com/press/press-releases/2026/more-than-10-million-developers-are-building-on-cloudflare (2026-06)
