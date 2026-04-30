def route_after_reasoning(state):
    if state["confidence"] < 0.93:
        return "second_opinion"
    return "merge"