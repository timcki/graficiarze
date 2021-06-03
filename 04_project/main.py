import numpy as np
from kosaraju import *

def main():
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

if __name__ == '__main__':
    main()   