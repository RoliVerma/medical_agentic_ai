def validation_agent(state):
    flags = []

    if state["confidence"] < 0.6:
        flags.append("Low confidence prediction")
    else:
        flags.append("High confidence prediction")
    return {"flags": flags}