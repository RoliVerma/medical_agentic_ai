import ollama

def report_agent(state):
    reasoning = state.get("final_reasoning") or state.get("reasoning")

    prompt = f"""
    Generate a structured radiology report.

    Input:
    {reasoning}

    Format:
    FINDINGS:
    IMPRESSION:
    RECOMMENDATIONS:
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "report": response["message"]["content"]
    }