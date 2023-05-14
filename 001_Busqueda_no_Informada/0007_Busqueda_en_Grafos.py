from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor, is_adjacent in enumerate(graph[node]):
            if is_adjacent and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

'''
     0
    / \
   1---2
  / \   \
 3---4---5

   0  1  2  3  4  5
0  0  1  1  0  0  0
1  1  0  1  1  1  0
2  1  1  0  0  0  1
3  0  1  0  0  1  0
4  0  1  0  1  0  1
5  0  0  1  0  1  0

'''

graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

bfs(graph, 0)
