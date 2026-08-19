import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class AiFinanceIntelligence:
    """AI Finance Intelligence Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # OpenRouter LLM setup
    llm = LLM(
        model="openrouter/openai/gpt-3.5-turbo",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
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