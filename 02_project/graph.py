from typing import List, Any

import random
import numpy as np

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, adj: Any):
        self.adjacency = adj
        self.size = adj.shape[0]

    # Algorithms taken from here:
    # https://math.stackexchange.com/questions/1074651/check-if-sequence-is-graphic-8-8-7-7-6-6-4-3-2-1-1-1
    # https://mathworld.wolfram.com/GraphicSequence.html
    @classmethod
    def from_sequence(cls, seq: List[int]) -> Any:

        if sum(seq) % 2:
            raise NotGraphicSequenceException()

        seq_copy = seq
        while True:
            seq_copy = -np.sort(-seq_copy)
            if seq_copy[0] == 0 and seq_copy[-1] == 0:
                return cls.adjacency_from_sequence(seq)

            k = seq_copy[0]
            seq_copy = seq_copy[1:]

            if k > len(seq_copy):
                raise NotGraphicSequenceException()

            for i in range(k):
                seq_copy[i] -= 1
                if seq_copy[i] < 0:
                    raise NotGraphicSequenceException()


    @classmethod
    def adjacency_from_sequence(cls, seq: List[int]) -> Any:

        a_matrix = np.zeros(shape=(len(seq), len(seq)), dtype=np.int8)
        seq = list(enumerate(-np.sort(-seq)))
        pos = 0

        while len(seq) > 0:
            edge, number = seq[0]
            seq = seq[1:]

            for i in range(0, number):
                seq[i] = (seq[i][0], seq[i][1]-1)
                a_matrix[edge, seq[i][0]] = a_matrix[seq[i][0], edge] = 1

            seq.sort(key=lambda x: -x[1])

        return cls(a_matrix)

    def randomize_edges(self):
        num_it = 0
        while num_it < 20000:
            num_it += 1
            while num_it < 20000:
                num_it += 1
                p1 = (random.randint(0, self.size-1), random.randint(0, self.size-1))
                if self.adjacency[p1[0], p1[1]] == 1 and p1[0] != p1[1]:
                    break
            while num_it < 20000:
                num_it += 1
                p2 = (random.randint(0, self.size-1), random.randint(0, self.size-1))
                if p2[0] not in p1 and p2[1] not in p1:
                    if self.adjacency[p2[0], p2[1]] == 1 and p2[0] != p2[1]:
                        break

            if self.adjacency[p1[0], p2[1]] == 1 or self.adjacency[p1[1], p2[0]] == 1: continue
            else: break

        if num_it >= 20000:
            return ((0, 0), (0, 0))


        # Set new edge pair
        # (a, b); (c, d) => (a, d); (b, c)
        self.adjacency[p1[0], p2[1]] = self.adjacency[p2[1], p1[0]] = 1
        self.adjacency[p1[1], p2[0]] = self.adjacency[p2[0], p1[1]] = 1
        # And delete previous one
        self.adjacency[p1[0], p1[1]] = self.adjacency[p1[1], p1[0]] = 0
        self.adjacency[p2[0], p2[1]] = self.adjacency[p2[1], p2[0]] = 0
        #print(p1, p2)
        return (p1, p2)

    def show(self):
        adj = self.adjacency
        print(adj)

        graph = nx.from_numpy_matrix(adj)
        plt.subplot(111)
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()



class NotGraphicSequenceException(Exception):
    pass