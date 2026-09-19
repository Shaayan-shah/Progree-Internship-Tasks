# Progree Artificial Intelligence — Task 3
# Heuristic Graph Pathfinding Agent Search Engine (A* & Dijkstra from Scratch)

import heapq
import time

class GridPathfindingAgent:
    def __init__(self, width=12, height=12, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles) if obstacles else set()

    def manhattan_heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in dirs:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in self.obstacles:
                neighbors.append((nx, ny))
        return neighbors

    def a_star_search(self, start, goal):
        start_time = time.perf_counter()
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        expanded_nodes = 0

        while open_set:
            _, current = heapq.heappop(open_set)
            expanded_nodes += 1

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                runtime_ms = (time.perf_counter() - start_time) * 1000
                return path, expanded_nodes, runtime_ms

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.manhattan_heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None, expanded_nodes, 0.0

if __name__ == "__main__":
    obstacles = [(3, y) for y in range(2, 9)] + [(7, y) for y in range(3, 10)]
    agent = GridPathfindingAgent(width=12, height=12, obstacles=obstacles)
    path, nodes, runtime = agent.a_star_search((1, 1), (10, 10))
    print(f"A* Path Found: {len(path)} steps in {runtime:.3f} ms (Expanded {nodes} nodes)")
