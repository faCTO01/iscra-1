from finance.binance_bot import BinanceBot
from finance.risk_manager import RiskManager

class AgentFactory:
    def __init__(self, permissions: dict, logs):
        self.registry = {}
        self.permissions = permissions
        self.logs = logs

    def create(self, spec: dict) -> str:
        role = spec.get("role", "dialog")
        agent_id = spec.get("id", f"agent_{len(self.registry)+1}")
        agent = {"role": role, "status": "pending"}

        if role == "trader":
            perms = self.permissions.get("agents", {}).get("trader", {})
            agent.update({
                "bot": BinanceBot(),
                "risk": RiskManager(
                    mode=perms.get("trading", "simulation_only").replace("_only", "")
                ),
            })

        self.registry[agent_id] = agent
        self.logs.write("agent_create", {"id": agent_id, "spec": spec})
        return agent_id

    def get(self, agent_id: str):
        return self.registry.get(agent_id)
