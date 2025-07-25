# 🧠 Intellectra — Autonomous Market Research & Risk Assessment Agent System

## Problem Statement

In today's dynamic market, startups and investors struggle to validate ideas or assess risks efficiently. Manual research, high-level analysis, and decision-making require time and domain expertise.

**Intellectra** solves this problem by enabling users to input product ideas and receive instant market analysis, risk assessment, and actionable business insights — powered by AI agents.

## 🚀 Why AI Agents?

AI agents are ideal for this use-case due to:

- **Autonomy**: Each agent performs a specialized task independently
- **Collaboration**: Multiple agents interact to deliver end-to-end insights
- **Scalability**: Easily extendable to include more expert agents (e.g., financial analyst, growth hacker)
- **Speed & Efficiency**: Reduces human hours in market research and de-risks early decisions

## 🔍 Use Case Summary

| Component       | Description                                                       |
|-----------------|-------------------------------------------------------------------|
| **Input**       | Problem statement or business idea (e.g., "Uber for rural India") |
| **Output**      | Market Research, Competitor Analysis, Risk Factors                |
| **Agents**      | Independent & Collaborative agents                                |
| **Ideal Users** | Entrepreneurs, Startup Founders, Investors                        |

## 🧩 Agents Architecture

### 👨‍💼 Agent Roles

| Agent Name                     | Responsibility                                                |
|--------------------------------|---------------------------------------------------------------|
| **Researcher Agent**           | Conducts domain-specific research related to the problem      |
| **Competitor Agent**           | Identifies and analyzes existing competitors and gaps         |
|  **Idea Improver Agent**       | Refines the original idea and adds innovative improvements    |
| **Tech Advisor Agent**         | Suggests suitable technology stacks, APIs, tools              |
| **Dev Architect Agent**        | Recommends architecture, databases, scalability plans         |
| **Feasibility Analyzer Agent** | Evaluates market feasibility, risks, and growth opportunities |
| **Summarizer Agent**           | Formats and compiles everything into a final readable summary |

### 🧠 How Agents Work

1. Each agent receives task-specific input from the Coordinator Agent
2. Agents independently utilize tools (search, LLMs) and return results
3. The Coordinator aggregates results, performs formatting, and generates a final summary

## 🛠 Tools, Libraries, and Frameworks

| Category            | Tools & Libraries Used                                    |
|---------------------|-----------------------------------------------------------|
| **Agent Framework** | CrewAI (multi-agent orchestration)                        |
| **Search Tools**    | SerperDevTool, TavilySearchTool (for Google-style search) |
| **Custom Tools**    | MarketResearcher, RiskAssessor (Domain-specific logic)    |
| **LLMs Tested**     | Gemini (via Google Cloud), Mixtral (Open Source)          |
| **Language**        | Python                                                    |

## 🤖 LLM Selection

### ✅ Final Free-tier LLMs Used

| LLM | Use-Case | Reason |
|-----|----------|---------|
| **Gemini (Google Cloud)** | General reasoning & formatting | Stable, fast, free |
| **Claude** | Summarization, formatting insights | Excellent coherence |
| **Perplexity API / Search-optimized models** | Real-time web data | Powerful factual accuracy |

### 🧠 Best LLMs for Ideal Version

| Model          | Justification                             |
|----------------|-------------------------------------------|
| **Claude 3**   | Most coherent for summarization & writing |
| **Perplexity** | Top-tier for live data + citations        |
| **Gemini Pro** | General-purpose reasoning & performance   |

## 🧪 How to Run the Project

```bash
git clone https://github.com/onlyprathamesh/Intellectra.git
cd Intellectra
python src/intellectra/main.py --problem "Build an app that solves..."
```

Make sure to configure your API keys for Gemini, Tavily, and Serper in `.env` as described below.

## ⚙️ Configuration

Create a `.env` file in the root directory:

```ini
TAVILY_API_KEY=your_key
SERPER_API_KEY=your_key
GEMINI_API_KEY=your_key
```

## 🌐 Deployment / Demo

You can run the project via CLI or easily wrap this into a Streamlit or Gradio UI for deployment on HuggingFace Spaces or Vercel.

**Demo Link**: Coming Soon

## 📂 Project Structure

```
├── src/
│   └── intellectra/
│       ├── agents.py           # Agent definitions
│       ├── tools.py            # Custom tools: MarketResearcher, RiskAssessor
│       ├── main.py             # Entry point
│       └── config.py           # CrewAI setup
├── README.md
└── requirements.txt
```

## 📌 Submission Details

- **Problem Statement**: Market validation for product ideas using multi-agent AI
- **AI Suitability**: Automates expert-like reasoning using domain-specialized agents
- **Free-Tier LLMs Used**: Gemini, Claude (via free APIs), Mixtral (initially)
- **Frameworks**: CrewAI, Langchain-compatible tools
- **GitHub Repo**: https://github.com/onlyprathamesh/Intellectra

## 🧠 Future Improvements

- [ ] Add UI/UX layer using Streamlit
- [ ] Expand agent pool (financial planner, legal advisor)
- [ ] Save agent insights to PDF / Notion
- [ ] Use vector store + RAG for PDF ingestion

## 🙏 Acknowledgments

Thanks to:

- **CrewAI** for orchestrating autonomous agents
- **Gemini API** for reliable LLM access
- **Open source community** for inspiration

---

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your API keys in `.env`
4. Run the system with your business idea
5. Get comprehensive market research and risk assessment!
