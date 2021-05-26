import numpy as np

def prim(G):
    mst = np.zeros(shape=G.adj.shape)
    T = np.array([0])
    W = np.array([i for i in range(1, len(G.adj))])

    while len(T) != len(G.adj):
        min = [-1, -1]
        for t in T:
            for w in W:
                if G.adj[t][w] != 0:
                    if min == [-1, -1] or G.adj[t][w] < G.adj[min[0]][min[1]]:
                        min = [t, w]
        
        mst[min[0]][min[1]] = mst[min[1]][min[0]] = G.adj[min[0]][min[1]]
        T = np.append(T, min[1])
        W = W[W != min[1]]
    
    return mst