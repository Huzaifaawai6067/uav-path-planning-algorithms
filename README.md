# uav-path-planning-algorithms
Comparison of Dijkstra and A* algorithms for UAV path planning in a grid environment with obstacles using Python and MATLAB.
# ✈️ UAV Path Planning Algorithms (Dijkstra vs A*)

## 📌 Overview

This project implements and compares path planning algorithms on a 2D grid environment with obstacles. The goal is to simulate how a UAV (drone) can find an optimal path from a start point to a destination while avoiding obstacles.

The project focuses on practical implementation and visualization rather than theoretical research.

---

## ⚙️ Features

* Grid-based environment with obstacles
* Implementation of:

  * Dijkstra’s Algorithm
  * A* (A-Star) Algorithm
* Path visualization
* Comparison of path efficiency and behavior
* MATLAB (for visualization/simulation) + Python (for algorithm implementation)

---

## 🛠️ Technologies Used

* Python (algorithm implementation)
* MATLAB (visualization and simulation)
* Graph-based pathfinding techniques

---

## 🧠 Algorithms Implemented

### 🔹 Dijkstra’s Algorithm

* Explores all possible paths
* Guarantees shortest path
* Slower in large grids

### 🔹 A* Algorithm

* Uses heuristic (distance to goal)
* Faster and more efficient
* Commonly used in real-world navigation

---

## 🔌 How It Works

1. A grid environment is created
2. Obstacles are placed within the grid
3. Start and goal positions are defined
4. Algorithms compute the path
5. Results are visualized using MATLAB



---

## 📊 Comparison

| Feature      | Dijkstra       | A*                |
| ------------ | -------------- | ----------------- |
| Speed        | Slower         | Faster            |
| Path Optimal | Yes            | Yes               |
| Efficiency   | Low            | High              |
| Use Case     | General graphs | Real-time systems |

---

## 📂 Repository Structure

* `/python` → Algorithm implementations
* `/matlab` → Visualization scripts
* `/images` → Output images and grid visuals

---

## 🚀 Future Improvements

* Add more algorithms (BFS, DFS, RRT)
* Introduce dynamic obstacles
* Extend to 3D UAV path planning
* Add real-time simulation

---

## 👨‍💻 Author

Muhammad Huzaifa Awais
Computer Engineering Student @ FAST-NUCES

---
