import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from components import Components
from dijkstra import Dijkstra
from centre import *
from mst import prim

class Graph:
    def __init__(self, n):
        self.prob = 0.5
        self.n = n
        self.adj = np.array([[0 for x in range(self.n)] for y in range(self.n)])
        self.rand_graph()
        self.biggest_comp = []
        self.choose_biggest_comp()
        self.assign_weights()

    def rand_graph(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                self.adj[i][j] = self.adj[j][i] = int(random.uniform(0, 1) <= self.prob)

    def choose_biggest_comp(self):
        adjacency = self.adj.tolist()
        components = Components()
        [comp, nr] = components.find_components(adjacency)

        for v in range(self.n):
            if comp[v] == components.max_component:
                self.biggest_comp.append(v)
        for i in reversed(range(self.n)):
            if i not in self.biggest_comp:
                adjacency.pop(i)
            else:
                for j in reversed(range(self.n)):
                    if j not in self.biggest_comp:
                        adjacency[i].pop(j)
        
        self.n -= (self.n - len(self.biggest_comp))
        self.adj = np.array(adjacency)

    def assign_weights(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.adj[i][j] != 0:
                    self.adj[i][j] = self.adj[j][i] = random.randint(1, 10)



def main():
    print('Podaj liczbę wierzchołków: ')
    n = int(input())
    G = Graph(n)
    print(f"Wylosowano graf o {G.n} wierzchołkach:")
    print(G.adj)

    print(f'Podaj wierzchołek startowy od 0 do {G.n - 1}: ')
    start = int(input())
    D = Dijkstra()
    D.do_dijkstra(G.adj, G.adj, start)

    print("START: s = " + str(start))
    for v in range(G.n):
        print(f'd({v}) = {D.ds[v]} ==> [', end='')
        print_ps(v, D)
        print(']')

    print("Macierz odległości:")
    matrix = make_distance_matrix(G)
    print(matrix)
    print("Centrum grafu:")
    print(get_center(matrix))
    print("Centrum minimax:")
    print(get_minimax_center(matrix))

    graph = nx.from_numpy_matrix(G.adj)
    graph.edges(data=True)
    plt.subplot(111)
    #nx.draw(graph, with_labels=True, font_weight='bold')
    pos=nx.circular_layout(graph)
    nx.draw_networkx(graph, pos)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

    print("Minimalne drzewo rozpinające:")
    mst = prim(G)
    print(mst)

    plt.subplot(111)
    graph = nx.from_numpy_matrix(G.adj)
    mst = nx.from_numpy_matrix(mst)

    pos = nx.circular_layout(graph)

    colors = []
    for u,v in graph.edges():
        if [u,v] not in mst.edges:
            colors.append('b')
        else:
            colors.append('r')

    graph.edges(data=True)
    nx.draw(graph, pos, with_labels=True, edge_color=colors)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def print_ps(v, D):
    if D.ps[v] != -1:
        print_ps(D.ps[v], D) 
        print(' - ', end='')
    print(v, end='')

if __name__ == '__main__':
	main()
        