import heapq

# Goal State
GOAL_STATE = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]


class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = 0   # f(n) = g(n) + h(n)

    # Display board
    def display(self):
        for i in range(0, 9, 3):
            print(self.state[i:i+3])
        print()

    # Check goal state
    def is_goal(self):
        return self.state == GOAL_STATE

    # Find position of blank (0)
    def get_blank_index(self):
        return self.state.index(0)

    # Generate successors
    def generate_successors(self):
        successors = []
        blank = self.get_blank_index()

        moves = {
            "UP": -3,
            "DOWN": 3,
            "LEFT": -1,
            "RIGHT": 1
        }

        for move, pos in moves.items():
            new_blank = blank + pos

            # Valid move conditions
            if move == "LEFT" and blank % 3 == 0:
                continue
            if move == "RIGHT" and blank % 3 == 2:
                continue
            if 0 <= new_blank < 9:
                new_state = self.state[:]
                new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
                successors.append(Puzzle(new_state, self, move, self.depth + 1))

        return successors

    # Heuristic: Manhattan Distance
    def heuristic(self):
        distance = 0
        for i in range(9):
            if self.state[i] != 0:
                goal_pos = GOAL_STATE.index(self.state[i])
                x1, y1 = divmod(i, 3)
                x2, y2 = divmod(goal_pos, 3)
                distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

    # f(n) = g(n) + h(n)
    def calculate_cost(self):
        self.cost = self.depth + self.heuristic()

    def __lt__(self, other):
        return self.cost < other.cost


# A* Search Algorithm
def a_star(initial_state):
    start = Puzzle(initial_state)
    start.calculate_cost()

    open_list = []
    heapq.heappush(open_list, start)

    visited = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            print("\n✅ Goal State Reached!\n")
            print_solution(current)
            return

        visited.add(tuple(current.state))

        for child in current.generate_successors():
            if tuple(child.state) not in visited:
                child.calculate_cost()
                heapq.heappush(open_list, child)

    print("❌ No solution found")


# Print solution path
def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print(f"Total moves: {len(path) - 1}\n")

    for step in path:
        print(f"Move: {step.move}")
        step.display()


# Input
print("Enter initial state (use 0 for blank):")
initial = list(map(int, input().split()))

a_star(initial)