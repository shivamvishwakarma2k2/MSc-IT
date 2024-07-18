visited = set()  # Set to keep track of visited nodes

def dfs(visited, graph, node):  # Function for DFS
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph = {
  1: [2, 3, 4],
  2: [5, 6],
  3: [],
  4: [7, 8],
  5: [9, 10],
  6: [],
  7: [11, 12],
  8: [],
  9: [],
  10: [],
  11: [],
  12: []
}

# Driver Code
print("Depth-First Search Result : ", end="")
dfs(visited, graph, 1)  # Function calling