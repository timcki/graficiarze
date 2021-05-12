#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException

import random
import numpy as np

def main():
    tries = 1
    for i in range(tries):
        el = np.array([random.randint(0, 9) for x in range(25)])
        #el = np.array([2, 2, 2, 2, 2, 2, 2])
        try:
            print(-np.sort(-el))
            g = Graph.from_sequence(el)
            for i in range(20):
                g.randomize_edges()
            for l in g.adjacency:
                for el in l:
                    print(el, end=',')
                print()
        except NotGraphicSequenceException:
            print("Not a graphic sequence")



if __name__ == '__main__':
    main()