#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from components import Components
from euler import euler
from hamilton import *

import argparse


def main():
    #test_all()

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--sequence', action='store_true',
                       help='''Check if given sequence is graphic. Sequence 
                        consisting of ints separated by spaces''')
    group.add_argument('-r', '--randomize', action='store_true',
                       help='''Randomize edges n times where n(int) is first parameter
                        after -r/--randomize flag
                        in graph given by the graphical sequence(ints separated by
                        spaces)''')
    group.add_argument('-c', '--composes', action='store_true',
                       help='''Find all connected  composes
                        in graph given by the graphical sequence(ints separated by
                        spaces) and mark the greatest''')
    group.add_argument('-e', '--euler', action='store_true',
                       help='''Make random Euler's graph with given n(int) nodes or
                        with random number of them if not specified''')
    group.add_argument('-kr', '--regular', action='store_true',
                       help='''Make k-regular graph with n nodes where k(int)is first
                        parameter and n(int) the second one''')
    group.add_argument('-H', '--hamilton', action='store_true',
                       help='''Check Hamilton's cycle exists in graph given by the
                        graphical sequence(ints separated by spaces) and prints it''')

    arg = parser.parse_known_args()

    if arg[0].sequence:
        parser2 = argparse.ArgumentParser()
        parser2.add_argument('seq', type=int, nargs='+')

        args = parser2.parse_args(arg[1])
        try:
            g = Graph.from_sequence(np.array(args.seq))
            g.show()

        except NotGraphicSequenceException:
            print(f"Sequence:\n{args.seq}\nis not a graphic sequence")
            return
        return

    if arg[0].randomize:
        parser2 = argparse.ArgumentParser()
        parser2.add_argument('n', type=int)
        parser2.add_argument('seq', type=int, nargs='+')

        args = parser2.parse_args(arg[1])
        if args.n < 0:
            print('Number of randomization n must be positive integer ')
            return

        try:
            g = Graph.from_sequence(np.array(args.seq))
        except NotGraphicSequenceException:
            print(f"Sequence:\n{args.seq}\nis not a graphic sequence")
            return

        print("Randomized edges:")
        for i in range(0, args.n):
            p1, p2 = g.randomize_edges()
            print(f"{p1}, {p2} => ({p1[0]}, {p2[1]}), ({p1[1]}, {p2[0]})")
        print()
        g.show()
        return

    if arg[0].composes:

        parser2 = argparse.ArgumentParser()
        parser2.add_argument('seq', type=int, nargs='+')

        args = parser2.parse_args(arg[1])

        try:
            g = Graph.from_sequence(np.array(args.seq))
        except NotGraphicSequenceException:
            print(f"Sequence:\n{args.seq}\nis not a graphic sequence")
            return

        G = g.adjacency

        components = Components()
        [comp, nr] = components.find_components(G)

        comp_lists = [[] for x in range(nr)]
        for v in range(len(G)):
            comp_lists[comp[v] - 1].append(v)

        for count, item in enumerate(comp_lists):
            print(count + 1, item)
        print("Biggest connected component: " + str(components.max_component))
        print("has " + str(components.max_count) + " vertices")
        return

    if arg[0].euler:
        # TO DO:: Implement this
        test_find_euler_random()
        return

    if arg[0].regular:
        print(5)
        parser2 = argparse.ArgumentParser()
        parser2.add_argument('n', type=int)
        parser2.add_argument('k', type=int)

        args = parser2.parse_args(arg[1])

        gen_k_regular(args.n, args.k)
        return

    if arg[0].hamilton:
        parser2 = argparse.ArgumentParser()
        parser2.add_argument('seq', type=int, nargs='+')

        args = parser2.parse_args(arg[1])
        try:
            g = Graph.from_sequence(np.array(args.seq))
        except NotGraphicSequenceException:
            print(f"Sequence:\n{args.seq}\nis not a graphic sequence")
            return
        adj_list = convert_matrix_to_adj_list(g.adjacency)
        print(adj_list)
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


def test_find_euler_random():
    print("\nTask 4: Euler cycle random:\n")
    #
    adjacency = np.array([[0, 1, 1, 1, 0, 1], 
         [1, 0, 1, 0, 0, 0], 
         [1, 1, 0, 1, 0, 1], 
         [1, 0, 1, 0, 1, 1], 
         [0, 0, 0, 1, 0, 1], 
         [1, 0, 1, 1, 1, 0]])
    g = Graph(adjacency)
    while True:
        n = random.randint(4, 10)
        el = np.array([random.randint(0, 4)*2 for x in range(n)])
        try:
            print(-np.sort(-el))
            g = Graph.from_sequence(el)
            #g = Graph.from_sequence(np.array([6, 6, 4, 2, 2, 2, 2, 2, 0]))
            choose_biggest_comp(g)
            print(g.adjacency)
            g.randomize_edges()
            for l in g.adjacency:
                for el in l:
                    print(el, end=',')
                print()
            graph = nx.from_numpy_matrix(g.adjacency)
            euler_list = []
            euler(g.adjacency.tolist(), 0, euler_list)
            print(euler_list)
                
            plt.subplot(111)
            nx.draw(graph, with_labels=True, font_weight='bold')
            plt.show()
            break
        except NotGraphicSequenceException:
            print("Not a graphic sequence")


if __name__ == '__main__':
    main()


def gen_k_regular(n, k):
    el = np.full(shape=n, fill_value=k, dtype=int)
    print(el)
    try:
        g = Graph.from_sequence(el)
    except NotGraphicSequenceException:
        print('It is impossible to create k-regular graph with given parameters!')
        return
    g.show()
    return


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

    g = {1: [2, 4, 5], 2: [1, 6, 5, 3], 3: [2, 7, 4], 4: [3, 1, 7, 6], 5: [2, 1, 8], 6: [4, 2, 8], 7: [4, 3, 8],
         8: [7, 6, 5]}
    g2 = {1: [2, 4], 2: [1, 3, 4, 5], 3: [2, 5], 4: [1, 2, 5], 5: [2, 3, 4]}
    g3 = {1: [2, 4], 2: [1, 4, 5], 3: [5], 4: [1, 2, 5], 5: [2, 3, 4]}

    check_hamilton_cycle(g)
    check_hamilton_cycle(g2)
    check_hamilton_cycle(g3)

    gen_k_regular(7, 2)
    gen_k_regular(4, 1)

def convert_matrix_to_adj_list(adj):
    l = {}
    for i in range (0, len(adj[0])):
        l[i + 1] = []
        for j in range(0, len(adj[0])):
            if adj[i][j] == 1:
                l[i + 1].append(j+1)
    return l

if __name__ == '__main__':
    main()
