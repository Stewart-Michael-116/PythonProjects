
# Example lists
state = [
    [1],
    [2],
    [2,3]]


GOAL = [
    [],
    [],
    [1,2,3]
]
def heuristic(GOAL, state):
    missing = len(GOAL[2]) - len(state[2])
    if missing == 3:
        return missing
    elif missing == 2:
        if state[2][0] == 3:
            return missing
        else:
            return 1 + missing
    elif missing == 1:
        if state[2] == [1,2]:
            return 3
        elif state[2] == [2,3]:
            return 1
        elif state[2] == [1,3]:
            return 2

print (heuristic(GOAL, state))