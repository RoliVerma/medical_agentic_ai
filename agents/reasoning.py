from openai import OpenAI

client = OpenAI()

def reasoning_agent(state):
    prompt = f"""
    You are a radiologist AI.

    Predictions: {state['predictions']}
    Confidence: {state['confidence']}

    Explain:
    - Likely findings
    - Clinical interpretation
    - Differential diagnosis
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "reasoning": response.choices[0].message.content
    }