import networkx as nx
import matplotlib.pyplot as plt

from graph import Graph
from dijkstra import Dijkstra
from centre import *
from mst import prim

def main():
    n = int(input('Podaj liczbę wierzchołków: '))
    G = Graph(n)
    G.rand_graph()
    G.choose_biggest_comp()
    G.assign_weights()
    print(f"Wylosowano graf o {G.n} wierzchołkach:")
    print(G)

    start = int(input(f'Podaj wierzchołek startowy od 0 do {G.n - 1}: '))
    D = Dijkstra()
    D.do_dijkstra(G.adj, G.adj, start)

    print(f"START: s = {start}")
    for v in range(G.n):
        print(f'd({v}) = {D.ds[v]} ==> [{get_ps(v, D)}]')

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


def get_ps(v, D):
    s = ''
    if D.ps[v] != -1:
        s += get_ps(D.ps[v], D) 
        s += ' - '
    s += str(v)
    return s

if __name__ == '__main__':
    main()
        