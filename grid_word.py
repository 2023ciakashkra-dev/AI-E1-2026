#program to represent a simple grid world environment similar to wumpus world and perform basic actions

import random

# Grid size
SIZE = 4

# Symbols
EMPTY = '.'
AGENT = 'A'
GOLD = 'G'
PIT = 'P'
WUMPUS = 'W'

class GridWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)

        # Place elements randomly
        self.place_random(GOLD)
        self.place_random(WUMPUS)
        for _ in range(2):
            self.place_random(PIT)

        self.grid[0][0] = AGENT

    def place_random(self, item):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[x][y] == EMPTY and (x, y) != (0, 0):
                self.grid[x][y] = item
                break

    def display(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def move_agent(self, direction):
        x, y = self.agent_pos
        self.grid[x][y] = EMPTY

        if direction == "up":
            x = max(0, x - 1)
        elif direction == "down":
            x = min(self.size - 1, x + 1)
        elif direction == "left":
            y = max(0, y - 1)
        elif direction == "right":
            y = min(self.size - 1, y + 1)

        self.agent_pos = (x, y)
        self.check_cell(x, y)
        self.grid[x][y] = AGENT

    def check_cell(self, x, y):
        cell = self.grid[x][y]

        if cell == GOLD:
            print("✨ You found the GOLD! You win!")
            exit()
        elif cell == PIT:
            print("💀 Fell into a PIT! Game over.")
            exit()
        elif cell == WUMPUS:
            print("👹 Eaten by the WUMPUS! Game over.")
            exit()
        else:
            self.sense(x, y)

    def sense(self, x, y):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        breeze = False
        stench = False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if self.grid[nx][ny] == PIT:
                    breeze = True
                if self.grid[nx][ny] == WUMPUS:
                    stench = True

        if breeze:
            print("🌬️ Breeze nearby (Pit is close)")
        if stench:
            print("💨 Stench nearby (Wumpus is close)")
        if not breeze and not stench:
            print("🙂 Safe cell")

# Run the environment
env = GridWorld(SIZE)

print("=== Grid World (Wumpus-like) ===")
env.display()

while True:
    move = input("Enter move (up/down/left/right): ").lower()
    if move in ["up", "down", "left", "right"]:
        env.move_agent(move)
        env.display()
    else:
        print("Invalid move!")