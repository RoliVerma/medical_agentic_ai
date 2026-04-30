def merge_agent(state):
    if state.get("second_opinion"):
        merged = f"""
Primary Opinion:
{state['reasoning']}

Second Opinion:
{state['second_opinion']}

Final Consensus:
Combine both opinions into a final clinical reasoning.
"""
    else:
        merged = state["reasoning"]

    return {
        "final_reasoning": merged
    }