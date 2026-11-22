# Specification: stam-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md`, `intent.md`)
- [x] Bootstrap agent code in `assets/stam-agent/` using instructions from the sap-agent-bootstrap section. (invoke from inside `assets/stam-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

No runtime skills required — the agent response is a simple fixed value with no branching logic.

---

## Project-Specific Tasks

## Fixed Response Implementation

- [x] Open `assets/stam-agent/app/agent.py`
- [x] Update the system prompt (`@prompt_section` / `get_system_prompt`) to instruct the agent: "Always respond with the exact text: stam. Do not add any other text, explanation, or formatting."
- [x] Ensure the agent returns "stam" for any user input, regardless of content

---

## Business Instrumentation

- [x] Add instrumentation for PRD milestones M1, M2 using `instrumentation.log_milestone` and named OpenTelemetry spans:
  - `M1.achieved: agent received user input` / `M1.missed: agent did not receive input or startup failed`
  - `M2.achieved: agent returned fixed response "stam"` / `M2.missed: agent failed to return response`
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

No MCP tools, SAP APIs, or external integrations required for this agent.

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write one integration test: call the agent's `invoke` function with any input, assert the response contains "stam". Mock the LLM to return "stam".
- [x] Run `pytest` from `assets/stam-agent/` (no args) — if coverage < 70%, add tests until threshold met
- [x] Run `pytest` again from `assets/stam-agent/` (no args) to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/stam-agent/`
