#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException
from components import Components
from euler import euler, choose_biggest_comp, print_m
from hamilton import *

import networkx as nx
import numpy as np
import click
import matplotlib.pyplot as plt

import random


@click.command()
@click.option('-s', '--sequence', type=str,
              help='''Check if sequence consisting of ints separated by commas
              is graphic, if true generates a graph.''')
@click.option('-f', '--filename', type=str,
              help='Read adjacency matrix representing graph from file')
@click.option('-r', '--randomize', type=int,
              help='Randomize edges n (int) times')
@click.option('-e', '--euler', 'euler_n', type=int,
              help='''Create a randomized Euler graph with given n (int) nodes
              or random n if unspecified''')
@click.option('-kr', '--regular', nargs=2, type=int,
              help='''Make k-regular graph with n nodes where n(int) is first
                        parameter and k(int) the second one''')
@click.option('-H', '--hamilton', is_flag=True,
              help='''Check if Hamilton cycle exists in given graph.
              If true prints it''')
@click.option('-c', '--components', is_flag=True,
              help='''Find all connected  components in given graph
              and mark the greatest''')
def parse_graph(sequence, filename, randomize, euler_n,
                regular, hamilton, components):
    if euler_n is not None:
        if euler_n == 0:
            euler_n = random.randint(5, 30)
        g = find_euler_random(euler_n)
        print(g)
        g.show()

        euler_list = []
        euler(g.adjacency.tolist(), 0, euler_list)

        print("Euler cycle:", ",".join([str(i) for i in euler_list]))
        return

    if regular != ():
        g = gen_k_regular(regular[0], regular[1])
        print(g)
        g.show()
        return

    if sequence is None and filename is None:
        click.echo("Please specify at least one input form")
    else:
        if sequence is not None:
            g = Graph.from_sequence(np.array([int(i) for i in sequence.split(',')]))
            if randomize is None:
                print(g)
                g.show()
        else:
            print(filename)

    if randomize is not None:
        print()
        print(g)
        print("Randomized edges:")
        for i in range(0, randomize):
            p1, p2 = g.randomize_edges()
            print(f"{p1}, {p2} => ({p1[0]}, {p2[1]}), ({p1[1]}, {p2[0]})")
        print()
        print(g)
        g.show()

    if components:
        G = g.adjacency

        components = Components()
        [comp, nr] = components.find_components(G)

        comp_lists = [[] for x in range(nr)]
        for v in range(len(G)):
            comp_lists[comp[v] - 1].append(v)

        print(f"Biggest connected component {components.max_component} has {components.max_count} vertices: ")
        for count, item in enumerate(comp_lists):
            print('\t', count + 1, item)
        print()

    if hamilton:
        adj_list = convert_matrix_to_adj_list(g.adjacency)
        check_hamilton_cycle(adj_list)
        return


def test_find_comp():
    print("\nTask 3: Connected components:\n")
    G = [[0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0]]

    components = Components()
    [comp, nr] = components.find_components(G)

    comp_lists = [[] for x in range(nr)]
    for v in range(len(G)):
        comp_lists[comp[v] - 1].append(v)

    for count, item in enumerate(comp_lists):
        print(count + 1, item)
    print("Biggest connected component: " + str(components.max_component))
    print("has " + str(components.max_count) + " vertices")


def test_find_euler():
    print("\nTask 4: Euler cycle:\n")
    G = [[0, 1, 1, 1, 0, 1],
         [1, 0, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1, 0]]

    matrix = np.array(G)
    graph = nx.from_numpy_matrix(matrix)

    euler_list = []
    euler(G, 0, euler_list)
    print(euler_list)

    plt.subplot(111)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


def find_euler_random(n):
    while True:
        el = np.array([random.randint(0, 4)*2 for x in range(n+1)])
        try:
            g = Graph.from_sequence(el)
            choose_biggest_comp(g)
            if g.adjacency.shape[0] != n:
                continue

            # Randomize graph
            for i in range(el.shape[0]*3):
                g.randomize_edges()
            return g
        except NotGraphicSequenceException:
            continue


def gen_k_regular(n, k) -> Graph:
    el = np.full(shape=n, fill_value=k, dtype=int)
    try:
        g = Graph.from_sequence(el)
        for i in range(20):
            g.randomize_edges()
    except NotGraphicSequenceException:
        print('It is impossible to create k-regular graph with given parameters!')
        return None
    return g


def test_all():
    tries = 3
    for i in range(tries):
        el = np.array([random.randint(0, 9) for x in range(25)])
        print(-np.sort(-el))
        try:
            g = Graph.from_sequence(el)
            for i in range(20):
                g.randomize_edges()
            g.show()
        except NotGraphicSequenceException:
            print("Not a graphic sequence")

    test_find_comp()
    test_find_euler()

    g = {1: [2, 4, 5], 2: [1, 6, 5, 3], 3: [2, 7, 4],
         4: [3, 1, 7, 6], 5: [2, 1, 8], 6: [4, 2, 8],
         7: [4, 3, 8], 8: [7, 6, 5]}
    g2 = {1: [2, 4], 2: [1, 3, 4, 5], 3: [2, 5], 4: [1, 2, 5], 5: [2, 3, 4]}
    g3 = {1: [2, 4], 2: [1, 4, 5], 3: [5], 4: [1, 2, 5], 5: [2, 3, 4]}

    check_hamilton_cycle(g)
    check_hamilton_cycle(g2)
    check_hamilton_cycle(g3)

    gen_k_regular(7, 2)
    gen_k_regular(4, 1)


def convert_matrix_to_adj_list(adj):
    a_list = {}
    for i in range(0, len(adj[0])):
        a_list[i + 1] = []
        for j in range(0, len(adj[0])):
            if adj[i][j] == 1:
                a_list[i + 1].append(j+1)
    return a_list


if __name__ == '__main__':
    parse_graph()
