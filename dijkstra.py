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
# 2. DIRECTIONS (4-connected)
# -----------------------------
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# -----------------------------
# 3. DIJKSTRA INITIALIZATION
# -----------------------------
dist = {start: 0}
parent = {}
priority_queue = []

heapq.heappush(priority_queue, (0, start))

# -----------------------------
# 4. DIJKSTRA ALGORITHM
# -----------------------------
while priority_queue:
    current_cost, current_node = heapq.heappop(priority_queue)

    if current_node == goal:
        break

    for d in directions:
        nr = current_node[0] + d[0]
        nc = current_node[1] + d[1]

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 0:
                new_cost = current_cost + 1
                neighbor = (nr, nc)

                if neighbor not in dist or new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    parent[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_cost, neighbor))

# -----------------------------
# 5. PATH RECONSTRUCTION
# -----------------------------
path = []
node = goal

while node != start:
    path.append(node)
    node = parent[node]

path.append(start)
path.reverse()

# -----------------------------
# 6. PLOTTING
# -----------------------------
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="gray_r")

y = [p[0] for p in path]
x = [p[1] for p in path]

plt.plot(x, y, color="red", linewidth=2, label="Path")
plt.scatter(start[1], start[0], c="green", s=100, label="Start")
plt.scatter(goal[1], goal[0], c="blue", s=100, label="Goal")

plt.title("Dijkstra Path Planning in 2D Grid")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.savefig("Figure_2_Dijkstra_Path.png")
plt.show()
