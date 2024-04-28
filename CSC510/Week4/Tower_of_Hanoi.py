
from __future__ import print_function
from simpleai.search import SearchProblem, astar
import copy


def list_to_string(list_):
    return '\n'.join(['-'.join(map(str, row)) if isinstance(row, list) and len(row) >= 3 else '-'.join(map(str, [0] * (3 - len(row)) + row)) if isinstance(row, list) else str(row) for row in list_])


def string_to_list(string_):
    return [[int(x) for x in row.split('-') if x != '0'] if row.strip() and row != '0-0-0' else [] for row in string_.split('\n')]

GOALL = [[],[],[1,2,3]]
INITIALL = [[1,2,3],[],[]]
GOAL = list_to_string(GOALL)
INITIAL = list_to_string(INITIALL)


class HelloProblem(SearchProblem):
    def actions(self, rows):
        actions = []
        state = string_to_list(rows)
        if state[0]:

            if not (state[1]) :
                temp = copy.deepcopy(state)
                temp[1].insert(0, temp[0].pop(0))
                actions.append(list_to_string(temp))
            elif(state[0][0]<state[1][0]):
                temp = copy.deepcopy(state)
                temp[1].insert(0, temp[0].pop(0))
                actions.append(list_to_string(temp))
            if (not state[2]):
                temp = copy.deepcopy(state)
                temp[2].insert(0, temp[0].pop(0))
                actions.append(list_to_string(temp))
            elif(state[0][0]<state[2][0]):
                temp = copy.deepcopy(state)
                temp[2].insert(0, temp[0].pop(0))
                actions.append(list_to_string(temp))

        if state[1]:

            if not (state[0]) :
                temp = copy.deepcopy(state)
                temp[0].insert(0, temp[1].pop(0))
                actions.append(list_to_string(temp))
            elif(state[1][0]<state[0][0]):
                temp = copy.deepcopy(state)
                temp[0].insert(0, temp[1].pop(0))
                actions.append(list_to_string(temp))
            if (not state[2]):
                temp = copy.deepcopy(state)
                temp[2].insert(0, temp[1].pop(0))
                actions.append(list_to_string(temp))
            elif(state[1][0]<state[2][0]):
                temp = copy.deepcopy(state)
                temp[2].insert(0, temp[1].pop(0))
                actions.append(list_to_string(temp))

        if state[2]:

            if not (state[0]) :
                temp = copy.deepcopy(state)
                temp[0].insert(0, temp[2].pop(0))
                actions.append(list_to_string(temp))
            elif(state[2][0]<state[0][0]):
                temp = copy.deepcopy(state)
                temp[0].insert(0, temp[2].pop(0))
                actions.append(list_to_string(temp))
            if (not state[1]):
                temp = copy.deepcopy(state)
                temp[1].insert(0, temp[2].pop(0))
                actions.append(list_to_string(temp))
            elif(state[2][0]<state[1][0]):
                temp = copy.deepcopy(state)
                temp[1].insert(0, temp[2].pop(0))
                actions.append(list_to_string(temp))
        return actions

    def result(self, state, action):

        return action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, rows):
        # how far are we from the goal? 
        #rows = rows[:-1] if rows.endswith('[') else rows
        state = string_to_list(rows)
        missing = int(len(GOALL[2]) - len(state[2]))
        return missing
        '''print(state)
        print("missing",missing)
        if missing == 3:
            return missing
        elif missing == 2:
            if state[2][0] == 3:
                return missing
            else:
                return 1 + int(missing)
        elif missing == 1:
            if state[2] == [1,2]:
                return 3
            elif state[2] == [2,3]:
                return 1
            elif state[2] == [1,3]:
                return 2'''
            


problem = HelloProblem(initial_state=INITIAL)
result = astar(problem)

print(result.state)
print(result.path())