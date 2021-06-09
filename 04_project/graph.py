from random import random
from collections import defaultdict

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, n: int):
        self.size = n
        self.adj_matrix = np.zeros((n, n), dtype=int)
        self.weights = np.random.randint(-5,11,(n,n))

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
        print(graph)
        plt.subplot(111)
        pos = nx.circular_layout(graph)
        nx.draw(graph, pos, with_labels=True, font_weight='bold')
        plt.show()

    def __str__(self):
        s = "\n"
        for row in self.adj_matrix:
            s += " ".join(str(i) for i in row)
            s += '\n'
        return s
