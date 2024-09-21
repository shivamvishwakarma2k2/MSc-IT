import heapq

def ao_star(start, goal, heuristic, neighbors):
    open_list = [(0, start)]  
# Priority queue initialized with the start node
    g_costs = {start: 0}  
# Dictionary to store the cost of the shortest path to each node
    came_from = {} 
 # Dictionary to reconstruct the path

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return list(reversed(path))  
# Return the path from start to goal
        
        for neighbor in neighbors(current):
            tentative_g = g_costs[current] + 1  
# Assuming uniform cost for each step
            if tentative_g < g_costs.get(neighbor, float('inf')):
                g_costs[neighbor] = tentative_g
                f_cost = tentative_g + heuristic(neighbor, goal)
                came_from[neighbor] = current
                heapq.heappush(open_list, (f_cost, neighbor))
    
    return None  
# Return None if no path is found

# Example usage:

def heuristic(point1, point2):
    # Manhattan distance heuristic for grid-based pathfinding
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def neighbors(node):
    # Example neighbor function for a grid (4-connected)
    x, y = node
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

# Example grid and start/goal points
start = (0, 0)
goal = (2, 2)

path = ao_star(start, goal, heuristic, neighbors)
print("Path found:", path)