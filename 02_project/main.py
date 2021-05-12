#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from components import Components 
from euler import euler, choose_biggest_comp

def main():
	tries = 1
	for i in range(tries):
		el = np.array([random.randint(0, 9) for x in range(25)])
		try:
			print(-np.sort(-el))
			g = Graph.from_sequence(el)
			g.randomize_edges()
			for l in g.adjacency:
				for el in l:
					print(el, end=',')
				print()
		except NotGraphicSequenceException:
			print("Not a graphic sequence")

	test_find_comp()
	test_find_euler()
	test_find_euler_random()


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
			#print(-np.sort(-el))
			#g = Graph.from_sequence(el)
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
			euler(g.adjacency, 0, euler_list)
			print(euler_list)
				
			plt.subplot(111)
			nx.draw(graph, with_labels=True, font_weight='bold')
			plt.show()
			break
		except NotGraphicSequenceException:
			print("Not a graphic sequence")


if __name__ == '__main__':
    main()