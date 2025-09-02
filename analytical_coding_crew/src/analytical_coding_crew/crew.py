from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
import os
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
)

load_dotenv()  

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators



@CrewBase
class AnalyticalCodingCrew():
    """AnalyticalCodingCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    llm = LLM(
        model = os.environ['MODEL'],    
        api_key = os.environ['GEMINI_API_KEY'],
        temperature = 0,

    )

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def analytical_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['analytical_agent'], # type: ignore[index]
            verbose=True,
            llm = self.llm,
            allow_code_execution=True,
            tools = [
                DirectoryReadTool(

                    directory='./data',
                ),

                FileReadTool(),
            ]
        )

    @agent
    def coding_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['coding_agent'], # type: ignore[index]
            verbose=True,
            llm = self.llm,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], # type: ignore[index]
        )

    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task'], # type: ignore[index]
            output_file='final_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AnalyticalCodingCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
