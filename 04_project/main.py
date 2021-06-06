import numpy as np
from kosaraju import *
from graph import Graph

def print_adj_list(adj_list):
    for k, v in adj_list:
        print(f"{k}: {v}")

if __name__ == '__main__':
    g = Graph(7)
    g.random_digraph(0.3)
    print(g)
    print_adj_list(g.adj_list.items())
    print('\nSilnie spójne składowe: ')
    kosaraju(g.adj_matrix)

    g.show()

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
