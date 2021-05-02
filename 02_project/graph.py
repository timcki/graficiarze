from typing import List, Any
import numpy as np

class Graph:
    def __init__(self, adj: Any):
        self.adjacency = adj

    # Algorithms taken from here:
    # https://math.stackexchange.com/questions/1074651/check-if-sequence-is-graphic-8-8-7-7-6-6-4-3-2-1-1-1
    # https://mathworld.wolfram.com/GraphicSequence.html
    @classmethod
    def from_sequence(cls, seq: List[int]) -> Any:

        if sum(seq) % 2:
            raise NotGraphicSequenceException()

        seq_copy = seq
        while True:

            print(seq_copy)
            seq_copy = -np.sort(-seq_copy)
            if seq_copy[0] == 0 and seq_copy[-1] == 0:
                return cls.adjacency_from_sequence(-np.sort(-seq))

            k = seq_copy[0]
            seq_copy = seq_copy[1:]

            if k > len(seq_copy):
                raise NotGraphicSequenceException()

            for i in range(k):
                seq_copy[i] -= 1
                if seq_copy[i] < 0:
                    raise NotGraphicSequenceException()

            print(seq_copy)


    @classmethod
    def adjacency_from_sequence(cls, seq: List[int]) -> Any:
        a_matrix = np.zeros(shape=(len(seq), len(seq)), dtype=np.int8)
        while True:

            seq_copy = -np.sort(-seq_copy)
            if seq_copy[0] == 0 and seq_copy[-1] == 0:
                return cls.adjacency_from_sequence(-np.sort(-seq))

            k = seq_copy[0]
            seq_copy = seq_copy[1:]

            for i in range(k):
                seq_copy[i] -= 1
                if seq_copy[i] < 0:
                    raise NotGraphicSequenceException()


        return cls(a_matrix)




class NotGraphicSequenceException(Exception):
    pass