#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException

import random
import numpy as np

def main():
	tries = 1
	for i in range(tries):
		el = np.array([random.randint(0, 9) for x in range(25)])
		try:
			g = Graph.from_sequence(el)
			print(g.adjacency)
		except NotGraphicSequenceException:
			print("Not a graphic sequence")



if __name__ == '__main__':
	main()