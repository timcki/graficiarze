import numpy as np

def dfs_stack(v, visited, stack, G):
    visited[v] = True
    for u in range(len(G)):
        if G[v][u] == 1 and visited[u] == False:
            dfs_stack(u, visited, stack, G)
    stack.append(v)

def dfs_print(v, visited, G):
    visited[v] = True
    print(v, end=' ')
    for u in range(len(G)):
        if G[v][u] == 1 and visited[u] == False:
            dfs_print(u, visited, G)

def transpose(G):
    GT = np.zeros(shape=G.shape)
    for v in range(len(G)):
        for u in range(len(G)):
            if G[v][u] == 1:
                GT[u][v] = 1
    return GT

def kosaraju(G):
    visited = [False for i in range(len(G))]
    stack = []
    for v in range(len(G)):
        if visited[v] == False:
            dfs_stack(v, visited, stack, G)
    GT = transpose(G)
    visited = [False for i in range(len(GT))]
    cn = 0
    while len(stack) > 0:
        v = stack.pop()
        if visited[v] == False:
            cn += 1
            print(f'{cn}: ', end='')
            dfs_print(v, visited, GT)
            print()