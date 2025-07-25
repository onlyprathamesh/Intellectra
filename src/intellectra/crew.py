from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from src.intellectra.tools.custom_tool import TavilySearch, MarketResearchTool, RiskAssessmentTool
from src.intellectra.llms import mixtral_llm1, mixtral_llm2, gemini2
serper_tool = SerperDevTool()
tavily_tool = TavilySearch()
market_research_tool = MarketResearchTool()
risk_assessment_tool = RiskAssessmentTool()

@CrewBase
class Intellectra():
    """Intellectra crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[serper_tool, tavily_tool]
        )
    @agent
    def competitor(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor'],
            verbose=True,
            tools=[serper_tool, tavily_tool, market_research_tool],
            llm=gemini2
        )
    @agent
    def idea_improver(self) -> Agent:
        return Agent(
            config=self.agents_config['idea_improver'],
            verbose=True
        )
    @agent
    def tech_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_advisor'],
            verbose=True,
            tools=[serper_tool],
            llm=gemini2
        )
    @agent
    def feasibility_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['feasibility_analyst'],
            verbose=True,
            tools=[risk_assessment_tool],
        )
    @agent
    def dev_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['dev_architect'],
            verbose=True,
            llm=gemini2
        )
    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            output_file='outputs/researcher_output.md'
        )
    @task
    def competitor_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitor_analysis_task'],
            output_file='outputs/competitor_output.md'
        )
    @task
    def idea_improvement_task(self) -> Task:
        return Task(
            config=self.tasks_config['idea_improvement_task'],
            output_file='outputs/idea_improver_output.md'
        )
    @task
    def tech_advisory_task(self) -> Task:
        return Task(
            config=self.tasks_config['tech_advisory_task'],
            output_file='outputs/tech_advisor_output.md'
        )
    @task
    def feasibility_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['feasibility_analysis_task'],
            output_file='outputs/feasibility_analyst_output.md'
        )
    @task
    def dev_planning_structuring_task(self) -> Task:
        return Task(
            config=self.tasks_config['dev_planning_structuring_task'],
            output_file='outputs/dev_architect_output.md'
        )
    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'],
            output_file='outputs/summarizer_output.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Intellectra crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
