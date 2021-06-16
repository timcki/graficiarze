import numpy as np
import copy

from graph import Graph
from kosaraju import *


class ExceededMaxIterations(Exception):
    pass


def relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w:
        d_s[v] = d_s[u] + w
        p_s[v] = u


def generate_connected_digraph(n, p):
    g = Graph(n)
    g.random_digraph(p)

    strongly_connected = kosaraju(g.adj_matrix, True)
    cycle_detected, ds, ps = bellman_ford(g, 0)

    i = 1
    while strongly_connected is not True or cycle_detected:
        g = Graph(n)
        g.random_digraph(p)

        strongly_connected = kosaraju(g.adj_matrix)
        cycle_detected, ds, ps = bellman_ford(g, 0)

        i += 1
        if i == 100000:
            raise ExceededMaxIterations(f"All {i} iterations did not generated strongly connected digraph")

    print(f"Number of iterations before generating strongly connected digraph: {i}")
    return g, ds, ps


def bellman_ford(g, start):
    """Returns if cycle with negative weight was detected """
    number_of_vertices, _ = g.adj_matrix.shape
    d_s = np.full(number_of_vertices, np.Inf)
    p_s = np.full(number_of_vertices, np.nan)
    d_s[start] = 0
    adj_list = g.gen_adj_list()

    for i in range(number_of_vertices - 1):
        for u in range(number_of_vertices):
            for v in adj_list[u]:
                relax(u, v, g.weights[u][v], d_s, p_s)

    for u in range(number_of_vertices):
        for v in adj_list[u]:
            if d_s[v] > d_s[u] + g.weights[u][v]:
                return True, d_s, p_s
    return False, d_s, p_s
