import networkx as nx
import matplotlib.pyplot as plt

from graph import Graph
from dijkstra import Dijkstra
from centre import *
from mst import prim

def main():
    n = int(input('Podaj liczbę wierzchołków: '))
    prob = float(input('Podaj prawdopodobieństwo wystąpienia krawędzi: '))
    G = Graph(n, prob)
    G.rand_graph()
    G.choose_biggest_comp()
    G.assign_weights()
    print(f"Wylosowano graf o {G.n} wierzchołkach:")
    print(G)

    print(f"Podaj wierzchołek startowy od 0 do {G.n - 1}: ")
    graph = nx.from_numpy_matrix(G.adj)
    graph.edges(data=True)
    plt.subplot(111)
    pos=nx.circular_layout(graph)
    nx.draw_networkx(graph, pos)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

    start = int(input())
    D = Dijkstra()
    D.do_dijkstra(G.adj, G.adj, start)

    print(f"START: s = {start}")
    for v in range(G.n):
        print(f'd({v}) = {D.ds[v]} ==> [{get_ps(v, D)}]')

    print("\nMacierz odległości:")
    matrix = make_distance_matrix(G)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(int(matrix[i][j]), end=' ')
            if int(matrix[i][j]) < 10:
                print(end=' ')
        print()
    
    centr = get_center(matrix)

    print(f"\nCentrum grafu: {centr}")
    print(f"Suma w centrum grafu: {sum(matrix[centr])}")
    minimax = get_minimax_center(matrix)

    print(f"\nCentrum minimax: {minimax}")
    print(f"Odległość do najdalszego wierzchołka: {max(matrix[minimax])}")

    print("\nMinimalne drzewo rozpinające:")
    [mst, sum_mst] = prim(G)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(int(matrix[i][j]), end=' ')
            if int(matrix[i][j]) < 10:
                print(end=' ')
        print()
    print(f"Suma wag krawędzi: {sum_mst}")

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
        