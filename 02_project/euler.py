from components import Components 
import numpy as np

#TO DO: losowanie grafu eulerowskiego z zad 2 o parzystych stopniach wierzcholkow i jednej spojnej skladowej
def euler(G, v, euler_list):
    euler_list.append(v)
    for u in range(len(G[v])):
        if G[v][u] == 1:
            is_bridge = bridge(G, v, u)
            if not is_bridge or (is_bridge and sum(i for i in G[v]) == 1):
                G[v][u] = 0
                G[u][v] = 0
                euler(G, u, euler_list)
        

def bridge(G, v, u):
    G[v][u] = 0
    G[u][v] = 0
    components = Components()
    [comp, nr] = components.find_components(G)
    G[v][u] = 1
    G[u][v] = 1
    if comp[v] != comp[u]:
        return True
    else:
        return False

def print_m(G):
    for v in range(len(G)):
        for u in range(len(G[v])):
            print(G[v][u], end='')
        print()

def choose_biggest_comp(G):
    biggest_comp = []
    components = Components()
    [comp, nr] = components.find_components(G.adjacency)

    adj = G.adjacency.tolist()
    for v in range(G.size):
        if comp[v] == components.max_component:
            biggest_comp.append(v)
    for i in reversed(range(G.size)):
        if i not in biggest_comp:
            adj.pop(i)
        else:
            for j in reversed(range(G.size)):
                if j not in biggest_comp:
                    adj[i].pop(j)
        
    G.size -= (G.size - len(biggest_comp))
    G.adjacency = np.array(adj)
