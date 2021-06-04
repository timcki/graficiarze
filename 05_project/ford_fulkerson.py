import numpy as np

def bfs(G, s, t):
    ds = [1000000000 for v in range(len(G))]
    ps = [None for v in range(len(G))]

    ds[s] = 0
    queue = []
    queue.append(s)
    while len(queue) > 0:
        v = queue.pop(0)
        if v == t:
            break
        for u in range(len(G)):
            if G[v][u] != 0 and ds[u] == 1000000000:
                ds[u] = ds[v] + 1
                ps[u] = v
                queue.append(u)

    v = t
    p = [v]
    while ps[v] != None:
        v = ps[v]
        p.insert(0, v)
    if len(p) == 1:
        p.pop()
    return p

def ford_fulkerson(G, s, t):
    f = [[0 for u in range(len(G))] for v in range(len(G))]
    Gf = np.copy(G) #cf

    p = bfs(Gf, s, t)
    print('p: ', p)
    while len(p) > 0:  
        cfp = Gf[p[0]][p[1]]
        for v in range(1, len(p) - 1):
            if Gf[p[v]][p[v+1]] < cfp:
                cfp = Gf[p[v]][p[v+1]]
        print('cfp: ', cfp)

        for v in range(0, len(p) - 1):
            if G[p[v]][p[v+1]] != 0:
                f[p[v]][p[v+1]] += cfp
            else:
                f[p[v+1]][p[v]] -= cfp
        #print('f: ', f)
        
        for v in range(len(G)):
            for u in range(len(G)):
                if G[v][u] != 0: #c
                    Gf[v][u] = G[v][u] - f[v][u]
                elif G[u][v] != 0:
                    Gf[v][u] = f[u][v]
                else:
                    Gf[v][u] = 0
        #print('Gf: ', Gf)
        
        p = bfs(Gf, s, t)
        print('p: ', p)
    return sum(f[0])
