import requests

def reasoning_agent(state):
    prompt = f"""
    You are a radiologist AI.

    Predictions: {state['predictions']}
    Confidence: {state['confidence']}

    Explain findings and diagnosis.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        # ✅ Safe parsing
        if "response" not in data:
            return {
                "reasoning": f"LLM Error: {data}"
            }

        return {
            "reasoning": data["response"]
        }

    except Exception as e:
        return {
            "reasoning": f"Exception: {str(e)}"
        }