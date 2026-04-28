import heapq

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def generate_successors(self):
        successors = []
        x, y = self.blank_pos

        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1)
        }

        for direction, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]

                tile_moved = new_state[new_x][new_y]  # tile coming into blank

                # Swap
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

                move_desc = f"Move {tile_moved} {direction}"

                successors.append(Puzzle(new_state, self, move_desc, self.depth + 1))

        return successors

    def __lt__(self, other):
        return False


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def a_star(initial_state):
    start = Puzzle(initial_state)

    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start.state), start))

    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        state_tuple = tuple(tuple(row) for row in current.state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current.is_goal():
            return current

        for neighbor in current.generate_successors():
            neighbor_tuple = tuple(tuple(row) for row in neighbor.state)

            if neighbor_tuple not in visited:
                cost = neighbor.depth + manhattan_distance(neighbor.state)
                heapq.heappush(open_list, (cost, neighbor))

    return None


# 🔹 UPDATED PRINT FUNCTION
def print_solution(goal_node):
    path = []
    current = goal_node

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    print("Initial State:")
    path[0].display()

    for i in range(1, len(path)):
        print(f"Move {i}: {path[i].move}")
        path[i].display()

    print("Goal State Reached!")


# Example
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    solution = a_star(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")