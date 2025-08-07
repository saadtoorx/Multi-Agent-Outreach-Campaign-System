---
title: "Multi-Agent Outreach Campaign System"
emoji: "📇"
colorFrom: "indigo"
colorTo: "red"
sdk: "streamlit"
sdk_version: "1.48.0"
app_file: "app.py"
pinned: true
---

# 📇 Multi-Agent Outreach Campaign System

An intelligent, modular multi-agent system for personalized lead generation and outreach — powered by [CrewAI](https://github.com/joaomdmoura/crewai). This project lets you simulate real-world sales representatives with goals, tools, and personas tailored to specific companies.

> Designed to identify valuable prospects and generate targeted, engaging outreach content with real-time data and AI.

---

## 🚀 Features

- 👥 **Company-Specific Agent Creation** – Auto-generates sales personas based on company (CrewAI, OpenAI, Google, etc.)
- 🔁 **Dynamic Task Flow** – From lead profiling to outreach content generation
- 🧠 **AI-Enhanced Agent Roles** – Equipped with detailed goals and backstories for realistic interactions
- 🧰 **Custom Tools** – Built-in file reading, web search, directory scanning, and sentiment analysis
- 🔧 **Plug-and-Play Structure** – Easily extendable for new companies or workflows

---

## 🏗️ Architecture Overview

### 🧠 Agents
- **Sales Representative Agent**: Discovers high-potential leads matching the company’s customer profile.
- **Lead Sales Representative Agent**: Crafts engaging outreach tailored to decision-makers.

These agents are pre-configured with:
- Personalized goals
- Company-specific backstories and references
- Delegation support and verbosity for transparency

### 📋 Tasks
1. **Lead Profiling** – Analyze a company's industry, achievements, and key players.
2. **Personalized Outreach** – Compose compelling email drafts using insights and sentiment analysis.

### 🛠️ Tools
- `DirectoryReadTool`: Reads context files from a directory
- `FileReadTool`: Extracts content from uploaded files
- `SerperDevTool`: Performs real-time web searches
- `SentimentAnalysisTool`: Analyzes tone of text (custom-built logic)

---

## 📁 Project Structure

```
lead-generation-crewai/
├── app.py                 # 🎯 Entry point to create agents and trigger logic
├── agents.py              # 🧠 Agent definitions based on company profiles
├── tasks.py               # 📋 Task setup and execution
├── tools.py               # 🧰 Custom and built-in tools used by agents
├── requirements.txt       # 📦 Dependencies list
├── README.md              # 📖 This file
└── instructions/          # 📂 Lead-specific instruction files (used by DirectoryReadTool)
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/saadtoorx/Multi-Agent-Outreach-Campaign-System.git
cd lead-generation-crewai
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
# or
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Configuration

Before running the app, make sure to have:

- `SERPER_API_KEY` for the search tool (from [Serper.dev](https://serper.dev/))

You’ll be prompted at runtime or can set it manually:
```bash
export SERPER_API_KEY=your-key        # Mac/Linux
# or
set SERPER_API_KEY=your-key           # Windows
```

---

## ▶️ Usage Example

```python
from agents import create_agents
from tasks import create_tasks

sales_agent, lead_agent = create_agents(company="Google")

inputs = {
    "lead_name": "NVIDIA",
    "industry": "AI Hardware",
    "key_decision_maker": "Jensen Huang",
    "position": "CEO",
    "milestone": "launch of new AI chip"
}

tasks = create_tasks(sales_agent, lead_agent, inputs)
```

Run tasks as needed using CrewAI TaskRunner or similar workflows.

---

## 🧠 Sample Output

### ✅ Lead Profiling Output
- Company: NVIDIA  
- Industry: AI Hardware  
- CEO: Jensen Huang  
- Recent News: Launched next-gen AI chip targeting LLM inference

### ✉️ Outreach Email Draft
> Subject: Unlocking AI Potential Together

Dear Jensen,

Congratulations on NVIDIA’s latest breakthrough in AI chip innovation! We believe there’s strong alignment between your mission and Google’s advancements in AI services. I’d love to explore how we can collaborate further...

---

## 📦 Tech Stack

- **Python 3.8+**
- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Serper API](https://serper.dev/)
- Custom Sentiment Tool (Pydantic + BaseTool)
- Directory & File Reader Tools (crewai_tools)

---

## 🔮 Future Enhancements

- 🧠 Add CRM data integrations
- 📨 Automate email sending via Gmail/Outlook API
- 📊 Visualize lead quality scoring
- 🧾 Save profiling and outreach logs

---

## 📄 License

Licensed under the MIT License. See [LICENSE](LICENSE) for full details.

---

## ✨ Created By

> Developed by [Saad Toor](https://www.linkedin.com/in/saadtoorx/)  
> AI-driven agent systems for smarter prospecting and outreach.
