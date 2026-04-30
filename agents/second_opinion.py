import ollama

def second_opinion_agent(state):
    prompt = f"""
    You are a SECOND radiologist.

    Review this case independently.

    Predictions: {state['predictions']}
    First opinion:
    {state['reasoning']}

    Provide an alternative or confirmatory interpretation.
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "second_opinion": response["message"]["content"]
    }