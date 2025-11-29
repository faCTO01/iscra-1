import requests
import json

def run_task(task):
    prompt = f"Проаналізуй задачу: {task['data']}"
    headers = {
        "Authorization": "Bearer ВСТАВ_ТУТ_OPENAGENTS_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4.1",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://api.openagents.io/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Помилка: {response.text}"
        def run_task(task):
    if task["type"] == "analyze_failure":
        return analyze_failure(task["log"])
    elif task["type"] == "retry_mission":
        return retry_mission()
        import json
from datetime import datetime

def run_task(task):
    if task["type"] == "analyze":
        return f"[AI-1] Аналіз завершено: {task['data']}"
    elif task["type"] == "analyze_failure":
        return f"[AI-1] Провал виявлено: {task['log']}"
    elif task["type"] == "retry_mission":
        return "[AI-1] Повторна спроба активована. Стратегія оновлена."
    else:
        return "[AI-1] Невідома задача"