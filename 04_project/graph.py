from random import random
from collections import defaultdict

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, n: int):
        self.size = n
        self.adj_matrix = np.zeros((n, n), dtype=int)

        self.rand_weight()

        self.adj_list = self.gen_adj_list()

    def random_digraph(self, p: float) -> None:
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    continue
                if random() <= p:
                    self.adj_matrix[i,j] = 1
        self.adj_list = self.gen_adj_list()

    def gen_adj_list(self):
        adj_list = defaultdict(list)
        for i in range(self.size):
            for j in range(i, self.size):
                if self.adj_matrix[i,j] == 1:
                    adj_list[i].append(j)
                if self.adj_matrix[j,i] == 1:
                    adj_list[j].append(i)
        return adj_list

    def show(self):
        graph = nx.from_numpy_matrix(self.adj_matrix, create_using=nx.DiGraph)

        dic = {}
        for i in range(self.size):
            for j in range(self.size):
                dic[(i, j)] = self.weights[i][j]

        nx.set_edge_attributes(graph, dic, 'weight')
        print(graph)

        print("Weights: ")
        s = "\n"
        for row in self.weights:
            s += " ".join(f'{i:2}' for i in row)
            s += '\n'

        print(s)

        plt.subplot(111)
        pos = nx.circular_layout(graph)
        nx.draw(graph.to_directed(), pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(graph.to_directed(), 'weight')
        nx.draw_networkx_edge_labels(graph.to_directed(), pos, edge_labels=labels)
        plt.show()

    def rand_weight(self):
        self.weights = np.random.randint(-5, 11, (self.size, self.size))  # np.random.randint(-5,11,(n,n))
        for i in range(self.size):
            self.weights[i][i] = 0
        # make weights symetric
        # self.weights = np.tril(self.weights) + np.triu(self.weights.T, 1)

        i = 0
        while i < self.size:
            self.weights[i][i] = 0
            i += 1

    def __str__(self):
        s = "\n"
        for row in self.adj_matrix:
            s += " ".join(str(i) for i in row)
            s += '\n'
        return s
