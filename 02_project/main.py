#! /usr/bin/python3

from graph import Graph, NotGraphicSequenceException
import random
import networkx as nx
import numpy as np
import random
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
			for i in range(20):
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
	while True:
		n = random.randint(4, 8)
		el = np.array([random.randint(0, 3)*2 for x in range(n)])
		try:
			print(-np.sort(-el))
			g = Graph.from_sequence(el)
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
			euler(g.adjacency.tolist(), 0, euler_list)
			print(euler_list)
				
			plt.subplot(111)
			nx.draw(graph, with_labels=True, font_weight='bold')
			plt.show()
			break
		except NotGraphicSequenceException:
			print("Not a graphic sequence")


if __name__ == '__main__':
    main()
