# FinAgent AI - Autonomous Financial Intelligence System
# LIVE DEMO : https://finagent-ai.streamlit.app/

FinAgent AI is an Agentic AI solution designed to automate financial data analysis, statistical reporting, and strategic budgeting insights. Built using CrewAI, Streamlit, and modern LLM integrations, it enables users to analyze financial CSV datasets or manual inputs through specialized autonomous AI agents.

## Author

* **Developer:** Insharah Syed
* **GitHub:** https://github.com/Insharah-syedd

## Key Features

* Multi-Agent Architecture: Utilizes CrewAI framework to orchestrate specialized agents for financial research and statistical summaries.
* Optimized Data Ingestion: Implements data compression techniques using Pandas to process large CSV files without exceeding token context limits.
* Interactive Dashboard: Features a clean Streamlit interface for seamless CSV uploads, manual input forms, and direct visualization of analysis results.
* Flexible LLM Integration: Built with LangChain and OpenRouter to support multiple large language models, including OpenAI GPT models.

## Architecture & Tech Stack

* Frontend: Streamlit
* Agentic Framework: CrewAI
* Data Processing: Python, Pandas
* Package Management: UV
* LLM Integration: OpenAI / OpenRouter API

## Project Structure

FinAgent-AI/
├── src/
│   └── ai_finance_intelligence/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       ├── crew.py
│       └── main.py
├── app.py
├── pyproject.toml
└── .env

## Local Installation & Setup

### Prerequisites

Ensure you have Python 3.10 or higher installed along with uv package manager.

pip install uv

### Installation Steps

1. Clone the repository:
git clone https://github.com/Insharah-syedd/FinAgent-AI.git
cd FinAgent-AI

2. Install dependencies:
uv sync

3. Set up environment variables:
Create a .env file in the root directory and configure your API credentials:
OPENAI_API_KEY=your_api_key_here

4. Run the Streamlit Application:
uv run streamlit run app.py

## Usage Instructions

1. Launch the web application in your browser (default: http://localhost:8501).
2. Select your preferred input method: Upload CSV or Enter Manually.
3. Upload a financial dataset (e.g., sales, expenses, or profit/loss records).
4. Review the data preview and click Analyze to generate agentic insights.
