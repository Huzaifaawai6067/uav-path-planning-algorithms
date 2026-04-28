import numpy as np
import matplotlib.pyplot as plt
import heapq

# -----------------------------
# 1. GRID DEFINITION
# 0 = free cell, 1 = obstacle
# -----------------------------
grid = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
])

start = (0, 0)
goal = (4, 4)

rows, cols = grid.shape

# -----------------------------
# 2. HEURISTIC FUNCTION
# Manhattan Distance
# -----------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# -----------------------------
# 3. DIRECTIONS (4-connected)
# -----------------------------
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# -----------------------------
# 4. A* INITIALIZATION
# -----------------------------
dist = {start: 0}        # g-cost
parent = {}
priority_queue = []

heapq.heappush(priority_queue, (0, start))

# -----------------------------
# 5. A* ALGORITHM
# -----------------------------
while priority_queue:
    current_f, current = heapq.heappop(priority_queue)

    if current == goal:
        break

    for d in directions:
        nr = current[0] + d[0]
        nc = current[1] + d[1]

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 0:
                g_cost = dist[current] + 1
                neighbor = (nr, nc)

                if neighbor not in dist or g_cost < dist[neighbor]:
                    dist[neighbor] = g_cost
                    parent[neighbor] = current
                    f_cost = g_cost + heuristic(neighbor, goal)
                    heapq.heappush(priority_queue, (f_cost, neighbor))

# -----------------------------
# 6. PATH RECONSTRUCTION
# -----------------------------
path = []
node = goal

while node != start:
    path.append(node)
    node = parent[node]

path.append(start)
path.reverse()

# -----------------------------
# 7. PLOTTING
# -----------------------------
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="gray_r")

y = [p[0] for p in path]
x = [p[1] for p in path]

plt.plot(x, y, color="blue", linewidth=2, label="A* Path")
plt.scatter(start[1], start[0], c="green", s=100, label="Start")
plt.scatter(goal[1], goal[0], c="red", s=100, label="Goal")

plt.title("A* Path Planning in 2D Grid")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.grid(True)
plt.legend()
plt.savefig("Figure_3_AStar_Path.png", dpi=300)
plt.show()
