# src/builder.py
import yaml
from jinja2 import Template
from crewai import Agent, Task

def render_yaml_template(file_path, context):
    with open(file_path, "r") as f:
        template = Template(f.read())
        rendered = template.render(**context)
        return yaml.safe_load(rendered)

def build_agents(config, llm):
    agents = {}
    for agent_conf in config["agents"]:
        agent = Agent(
            role=agent_conf["role"],
            goal=agent_conf["goal"],
            backstory=agent_conf["backstory"],
            verbose=agent_conf.get("verbose", False),
            llm=llm
        )
        agents[agent_conf["name"]] = agent
    return agents

def build_tasks(config, agents):
    tasks = []
    for task_conf in config.get("tasks", []):
        task = Task(
            description=task_conf["description"],
            agent=agents[task_conf["agent"]],
            expected_output=task_conf.get("expected_output", "A detailed response fulfilling the task goal.")
        )
        tasks.append(task)
    return tasks
