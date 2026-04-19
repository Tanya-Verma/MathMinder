import requests

def generate_steps(problem):
    prompt = f"Solve step by step: {problem}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt
        }
    )

    return response.json()["response"]