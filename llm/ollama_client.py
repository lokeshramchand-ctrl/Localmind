import requests

def ask_llm(context, question):
    prompt = f"""
Context:
{context}

Question:
{question}
"""

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]
