#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from components import Components
from euler import euler
from hamilton import *

def main():
	# tries = 1
	# for i in range(tries):
	# 	el = np.array([random.randint(0, 9) for x in range(25)])
	# 	print(el)
	# 	try:
	# 		g = Graph.from_sequence(el)
	# 		print(g.adjacency)
	# 	except NotGraphicSequenceException:
	# 		print("Not a graphic sequence")
	#
	tries = 200
	su = 0
	for i in range(tries):
		el = [random.randint(0, 6) for x in range(10)]
		su += int(check_seq(el))
	print(su / tries)

	test_find_comp()
	test_find_euler()

	g = {1: [2,4,5], 2: [1,6,5,3], 3: [2,7,4], 4: [3,1,7,6], 5:[2,1,8], 6:[4,2,8], 7:[4,3,8], 8:[7,6,5]}
	g2 = {1:[2,4], 2: [1,3,4,5], 3:[2,5], 4:[1,2,5], 5:[2,3,4]}
	g3 = {1: [2, 4], 2: [1, 4, 5], 3: [5], 4: [1, 2, 5], 5: [2, 3, 4]}

	check_hamilton_cycle(g)
	check_hamilton_cycle(g2)
	check_hamilton_cycle(g3)

	# gen_k_regular(7, 2)




def check_seq(seq):
	if sum(seq) % 2:
		return False
	return True


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


def gen_k_regular(n, k):
	el = np.ones(n) * k
	el = [int(x) for x in el]
	print(el)
	g = Graph.from_sequence(el)
	print(g.adjacency)

if __name__ == '__main__':
	main()