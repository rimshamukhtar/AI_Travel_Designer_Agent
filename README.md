# 🧳 AI Travel Designer Agent

Design custom travel itineraries powered by multi-agent AI workflows!

---

## 📌 Overview
This project is a multi-agent AI application built using the **OpenAI Agent SDK** and **Chainlit**. The AI Travel Designer agent helps users plan travel experiences by dynamically switching between specialized agents:

- 🗺️ **PlannerAgent** — Suggests destinations, builds trip structure.
- 💰 **BudgetAgent** — Optimizes costs and budget.
- 🎒 **PackingAgent** — Provides customized packing lists.

### 🔁 Agent Orchestration
The system uses the Agent SDK's `Runner` to coordinate these agents, enabling **handoff** logic where one agent passes the conversation to another based on context.

---

## 🔧 Tools Used
- **OpenAI Agent SDK** — For agent logic, handoffs, tracing.
- **Chainlit** — For real-time interactive UI.
- **dotenv** — For secure API key management.

---

## 📂 Folder Structure
```
AI_Travel_Designer/
├── main.py                # Chainlit + orchestration logic
├── model_loader.py       # Model initialization
├── tools.py              # Custom tools if any
├── travel_agents/
│   ├── planner_agent.py
│   ├── budget_agent.py
│   └── packing_agent.py
├── .env
└── README.md             # You're reading this!
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd AI_Travel_Designer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add `.env` File
```
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run Chainlit
```bash
chainlit run main.py
```
Visit `http://localhost:8000` to chat with your travel agent.

---

## 💡 Example Commands
```
"Plan a 5-day trip to Tokyo under $1500"
"Suggest summer vacation spots in Europe"
"What should I pack for Iceland in winter?"
```

---

## 🧠 How Handoff Works
- `PlannerAgent` detects budget-related queries ➜ hands off to `BudgetAgent`
- `BudgetAgent` completes cost suggestions ➜ returns to `PlannerAgent`
- `PlannerAgent` detects packing concerns ➜ hands off to `PackingAgent`

Each handoff is handled via `Runner.run()` with clear agent roles.

---

## 🌐 Tech Stack
- Python 3.10+
- [OpenAI Agent SDK](https://github.com/openai/agents)
- [Chainlit](https://github.com/Chainlit/chainlit)

---

## 🙋‍♀️ Built By
**Rimsha MUkhtar**

