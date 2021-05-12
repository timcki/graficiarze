from typing import List, Any

import random
import numpy as np

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
        seq = -np.sort(-seq)
        pos = 0

        while len(seq) > 0:

            k = seq[0]
            seq = seq[1:]

            for i in range(0, k):
                inc = i
                while inc < len(seq):
                    if seq[inc] > 0:
                        seq[inc] -= 1
                        break
                    else:
                        inc += 1
                a_matrix[pos][inc+1+pos] = a_matrix[inc+1+pos][pos] = 1

            pos += 1

        return cls(a_matrix)

    def randomize_edges(self):
        while True:
            p1 = (random.randint(1, self.size-1), random.randint(1, self.size-1))
            if self.adjacency[p1[0]][p1[1]] == 1:
                break
        while True:
            p2 = (random.randint(1, self.size-1), random.randint(1, self.size-1))
            if p2[0] not in p1 and p2[1] not in p1:
                if self.adjacency[p2[0]][p2[1]] == 1:
                    break
        # Set new edge pair
        # (8, 3); (1, 13)
        # (8, 13); (1, 3)
        self.adjacency[p1[0], p2[1]] = self.adjacency[p2[1], p1[0]] = 1
        self.adjacency[p2[0], p1[1]] = self.adjacency[p1[1], p2[0]] = 1
        # And delete previous one
        self.adjacency[p1[0], p1[1]] = self.adjacency[p1[1], p1[0]] = 0
        self.adjacency[p2[0], p2[1]] = self.adjacency[p2[1], p2[0]] = 0
        print(p1, p2)




class NotGraphicSequenceException(Exception):
    pass