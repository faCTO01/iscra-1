import json
import importlib

def load_agents():
    with open("agent_manifest.json", "r") as f:
        manifest = json.load(f)
    agents = {}
    for agent in manifest["agents"]:
        if agent["status"] == "active":
            module = importlib.import_module(agent["module"].replace(".py", ""))
            agents[agent["id"]] = module
    return agents