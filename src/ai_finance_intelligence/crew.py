import os

from dotenv import load_dotenv
from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()


def get_gemini_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing Gemini API key. Set GEMINI_API_KEY or GOOGLE_API_KEY in your environment or .env file."
        )
    return api_key


@CrewBase
class AiFinanceIntelligence:
    """AI Finance Intelligence Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    llm = LLM(
        model="gemini/gemini-3.6-flash",
        api_key=get_gemini_api_key(),
        temperature=0.2,
    )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_researcher"],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_analyst"],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def financial_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_advisor"],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    @task
    def collect_financial_information(self) -> Task:
        return Task(
            config=self.tasks_config["collect_financial_information"]
        )

    @task
    def analyze_financial_health(self) -> Task:
        return Task(config=self.tasks_config["analyze_financial_health"])

    @task
    def create_financial_plan(self) -> Task:
        return Task(config=self.tasks_config["create_financial_plan"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False,
        )