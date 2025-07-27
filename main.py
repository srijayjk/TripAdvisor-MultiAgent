# main.py
import os
from dotenv import load_dotenv
from src.builder import render_yaml_template, build_agents, build_tasks
from crewai import Crew
from langchain_community.llms import Ollama


if __name__ == "__main__":
    # Step 1: Get user inputs
    destination = input("Where are you traveling? ")
    days = input("How many days? ")
    budget = input("What is your total budget in USD? ")

    context = {
        "destination": destination,
        "days": days,
        "budget": budget
    }

    # Step 2: Load and render agent config
    yaml_path = os.path.join("config", "agents_config.yaml")
    config = render_yaml_template(yaml_path, context)

    # Step 3: Initialize LLM
    llm = "ollama/llama3.2:3b"
    
    # Step 4: Build agents and tasks
    agents = build_agents(config, llm)
    tasks = build_tasks(config, agents)

    # Step 5: Run the Crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    results = crew.kickoff()
    print("\n\nFinal Result:\n", results)
