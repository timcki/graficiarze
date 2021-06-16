import numpy as np
from kosaraju import *
from graph import Graph

from johnson import *
from bellman_ford import *

def print_adj_list(adj_list):
    for k, v in adj_list:
        print(f"{k}: {v}")

if __name__ == '__main__':
    nr_of_vertices = 3
    p = 0.5

    g = Graph(nr_of_vertices)
    g.random_digraph(p)
    print('\n1.Kodowanie digrafów; generowanie digrafów losowych G(n,p)')
    print(g)
    print_adj_list(g.adj_list.items())
    print('\n2.Silnie spójne składowe: ')
    kosaraju(g.adj_matrix, True)

    g.show()

    print("3. Silnie spójny digraf\n")
    try:
         g, ds, ps = generate_connected_digraph(nr_of_vertices, p )
    except ExceededMaxIterations as e:
        print("***\n","ExceededMaxIterations", "Exiting program...")
        exit(1)

    g.gen_adj_list()
    print(g)
    print_adj_list(g.adj_list.items())
    print('\nSilnie spójne składowe: ')
    kosaraju(g.adj_matrix, True)
    g.show()

    print("Najkrótsza ścieżka:", ds, '\n')
    print("Previous nodes in shortest paths:", ps, '\n')

    print("4.Macierz odległości\n")
    print("Distance matrix from Johnson algorithm:")
    d = johnson(g)
    for x in d:
        x = [a if a < 100000 else a - 1000000 for a in x]
        print(x)


def test():
    G = [
        [0, 1, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
    ]

    G2 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]

    G3 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]

    kosaraju(np.array(G))
    kosaraju(np.array(G2))
    kosaraju(np.array(G3))
