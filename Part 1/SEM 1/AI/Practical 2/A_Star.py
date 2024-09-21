import heapq
import math

def heuristic_distance(point1, point2):
    # using manhaten distance
    # return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    # using eucledian distance
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def a_star(grid, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in grid}
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = current[0] + dx, current[1] + dy
            if neighbor in grid:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_list, (g_score[neighbor] + heuristic_distance(neighbor, goal), neighbor))

    return None  # No path found

# Example grid (dict with (x, y) as keys)
grid = {
    (0, 0), (0, 1), (0, 2),(0,3),
    (1, 0), (1, 1), (1, 2),(1,3),
    (2, 0), (2, 1), (2, 2),(2,3)
}

start = (1, 0)
goal = (0, 3)
path = a_star(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")