from openai import OpenAI

client = OpenAI()

def report_agent(state):
    prompt = f"""
    Generate a radiology report.

    Reasoning:
    {state['reasoning']}

    Format:
    FINDINGS:
    IMPRESSION:
    RECOMMENDATIONS:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "report": response.choices[0].message.content
    }