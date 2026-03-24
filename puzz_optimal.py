import heapq

GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class Puzzle:
    def __init__(self, state, parent=None, move="", moved_tile=None, g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.moved_tile = moved_tile
        self.g = g
        self.h = self.manhattan()
        self.f = self.g + self.h

    # Manhattan Distance
    def manhattan(self):
        distance = 0
        for i in range(9):
            if self.state[i] != 0:
                goal_index = GOAL.index(self.state[i])
                x1, y1 = divmod(i, 3)
                x2, y2 = divmod(goal_index, 3)
                distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

    def is_goal(self):
        return self.state == GOAL

    def neighbors(self):
        result = []
        idx = self.state.index(0)

        moves = {
            "UP": -3,
            "DOWN": 3,
            "LEFT": -1,
            "RIGHT": 1
        }

        for move, pos in moves.items():
            new_idx = idx + pos

            if move == "LEFT" and idx % 3 == 0:
                continue
            if move == "RIGHT" and idx % 3 == 2:
                continue
            if 0 <= new_idx < 9:
                new_state = self.state[:]

                # tile being moved
                moved_tile = new_state[new_idx]

                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]

                result.append(Puzzle(new_state, self, move, moved_tile, self.g + 1))

        return result

    def __lt__(self, other):
        return self.f < other.f


def a_star(start_state):
    start = Puzzle(start_state)

    open_list = []
    heapq.heappush(open_list, start)

    visited = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            print("\n✅ Goal Reached!\n")
            print_solution(current)
            return

        visited.add(tuple(current.state))

        for neighbor in current.neighbors():
            if tuple(neighbor.state) not in visited:
                heapq.heappush(open_list, neighbor)

    print("❌ No solution found")


def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print("Initial State:")
    display(path[0].state)

    for i in range(1, len(path)):
        step = path[i]
        print(f"Move {i}: Move {step.moved_tile} {step.move.lower()}")
        display(step.state)


def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# 🔹 Given Example Initial State
initial_state = [1, 2, 3,
                 4, 0, 6,
                 7, 5, 8]

a_star(initial_state)