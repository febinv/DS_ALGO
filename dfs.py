def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)
    return visited


graph={0: [1, 2], 1: [3,4], 2: [5],3:[],4:[],5:[]}
#bfs(graph,0)
print(dfs(graph,0,[]))
