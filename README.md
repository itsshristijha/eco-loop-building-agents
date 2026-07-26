# 🏢 Eco-Loop Building Agents

## AI-Powered Autonomous Building Management System

### Overview

Eco-Loop Building Agents is an AI-driven smart building management system developed for the Honeywell Hackathon.

The system simulates a commercial building, continuously monitors environmental conditions, analyses them using an AI agent, and recommends HVAC actions to improve occupant comfort while reducing energy consumption.

---

## Features

- Real-time building monitoring
- AI-powered HVAC recommendations
- FastAPI backend
- Streamlit dashboard
- Simulated EnergyPlus integration
- Modular controller architecture
- GitHub-ready project structure

---

## Technology Stack

- Python
- FastAPI
- Streamlit
- Plotly
- Pandas
- Requests
- Git
- GitHub

Future Integration

- EnergyPlus
- Model Context Protocol (MCP)
- Open Source LLM (Qwen/Llama)
- Ollama

---

## Project Structure

```
eco-loop-building-agents
│
├── app.py
├── dashboard.py
├── controller.py
├── energyplus_wrapper.py
├── agent.py
├── mcp_server.py
├── requirements.txt
├── README.md
├── docs/
└── data/
```

---

## System Workflow

```
Building Data
      │
      ▼
EnergyPlus Wrapper
      │
      ▼
Controller
      │
      ▼
AI Agent
      │
      ▼
HVAC Recommendation
      │
      ▼
Dashboard
```

---

## API

### GET /

Returns API status.

### GET /simulate

Returns

- Temperature
- Humidity
- Occupancy
- Energy Consumption
- AI HVAC Recommendation

---

## Dashboard

Displays

- Temperature
- Humidity
- Occupancy
- Energy Consumption
- AI Recommendation
- Live Energy Trend
- Live Temperature Trend

---

## Future Scope

- Integrate EnergyPlus
- Connect Open Source LLM
- MCP Tool Calling
- Carbon Emission Optimisation
- Predictive Energy Analytics

---

## Team

Honeywell Eco-Loop Building Agents Hackathon Submission