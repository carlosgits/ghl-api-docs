# Agents

Source: https://marketplace.gohighlevel.com/docs/ghl/agent-studio/agents

Screenshot: C:\Users\carlo\OneDrive\Desktop\Proyectos\ghl-api-docs\images\ghl_agent-studio_agents_screenshot.png

---

AI Agent StudioAgents
Agents
Documentation for Agent Studio APIs
📄️ List Agents
Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset.
📄️ Get Agent
Gets a specific agent by its ID for the specified location. locationId is required parameter. The agent must have active status.
📄️ Execute Agent
Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.