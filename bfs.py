import collections

def bfs(graph,root):
    visited,queue=set(),collections.deque([root])
    while queue:
        vertex=queue.popleft()
        print(vertex)
        for neighbours in graph[vertex]:
            if neighbours not in visited:
                visited.add(neighbours)
                queue.append(neighbours)


graph={0: [1, 2], 1: [3,4], 2: [5],3:[],4:[],5:[]}
bfs(graph,0)
#print(dfs(graph,0,[]))
