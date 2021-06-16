import numpy as np

from graph import Graph
from bellman_ford import bellman_ford
from dijkstra import Dijkstra


def add_s(g):
    number_of_vertices, _ = g.adj_matrix.shape
    w_tmp = np.zeros((number_of_vertices + 1, number_of_vertices + 1))
    adj_tmp = np.zeros((number_of_vertices + 1, number_of_vertices + 1))
    for i in range(number_of_vertices):
        w_tmp[i] = np.insert(g.weights[i], number_of_vertices, 0)
        adj_tmp[i] = np.insert(g.adj_matrix[i], number_of_vertices, 0)

    column = [1] * (number_of_vertices + 1)
    column[number_of_vertices] = 0
    adj_tmp[number_of_vertices] = np.asarray(column)

    g.adj_matrix = adj_tmp
    g.weights = w_tmp
    g.size = g.size + 1
    g.gen_adj_list()

    # print("\n\n### ADING###\n")
    # print(g.weights)
    # print_adj_list(g.adj_list.items())
    # print('\nSilnie spójne składowe: ')
    # kosaraju(g.adj_matrix, True)
    # g.show()


def johnson(g):
    """Function generating distance matrix for weighted graph"""
    number_of_vertices, _ = g.adj_matrix.shape
    add_s(g)

    w_dashed = np.zeros((number_of_vertices + 1, number_of_vertices + 1))

    cycle_detected, ds, ps = bellman_ford(g, number_of_vertices)
    # print("***\n", ds, "***\n")

    if cycle_detected:
        raise ValueError('A negative cycle has been found in the graph. Johson algoritm stopped.')

    for u in range(number_of_vertices + 1):
        for v in range(number_of_vertices + 1):
            if g.adj_matrix[u][v] == 1:
                w_dashed[u][v] = g.weights[u][v] + ds[u] - ds[v]

    d = np.zeros((number_of_vertices, number_of_vertices))

    for u in range(number_of_vertices):
        dijkstra = Dijkstra()
        dijkstra.do_dijkstra(g.adj_matrix, g.adj_matrix, u+1)
        distance = dijkstra.ds

        for v in range(number_of_vertices):
            d[u][v] = distance[v] - ds[u] + ds[v]

    return d
