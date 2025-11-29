import requests
import json

def run_task(task):
    prompt = f"Згенеруй код або креслення для: {task['data']}"
    headers = {
        "Authorization": "Bearer ВСТАВ_ТУТ_DIFY_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": {"question": prompt}
    }
    response = requests.post("https://api.dify.ai/v1/chat-messages", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["answer"]
    else:
        return f"Помилка: {response.text}"
        def run_task(task):
    if task["type"] == "generate_code":
        return f"[AI-2] Згенеровано код для: {task['data']}"
    elif task["type"] == "build_strategy":
        return "[AI-2] Стратегія побудована: скальпінг + спрінт"
    else:
        return "[AI-2] Невідома задача"