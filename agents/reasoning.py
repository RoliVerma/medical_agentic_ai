import ollama

def reasoning_agent(state):
    prompt = f"""
    You are a radiologist AI.

    Predictions: {state['predictions']}
    Confidence: {state['confidence']}

    Provide clinical reasoning.
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "reasoning": response["message"]["content"]
    }