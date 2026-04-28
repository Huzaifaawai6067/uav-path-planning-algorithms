import numpy as np
import matplotlib.pyplot as plt

# 1. UAV environment (0 = free, 1 = obstacle)
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

grid = np.array(grid)

# 2. Start and goal positions
start = (0, 0)
goal = (4, 4)

# 3. Create figure
plt.figure(figsize=(5, 5))
plt.imshow(grid, cmap="gray_r")

# 4. Plot start and goal
plt.scatter(start[1], start[0], c='green', s=100, label="Start")
plt.scatter(goal[1], goal[0], c='red', s=100, label="Goal")

# 5. Labels
plt.title("2D UAV Environment with Obstacles")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

# 6. Save image for paper
plt.savefig("Figure_1_UAV_Grid.png", dpi=300)

# 7. Show plot
plt.show()
