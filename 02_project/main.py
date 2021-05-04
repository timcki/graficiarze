import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from components import Components 
from euler import euler

def main():
	tries = 200
	su = 0
	for i in range(tries):
		el = [random.randint(0, 6) for x in range(10)]
		su += int(check_seq(el))
	print(su/tries)

	test_find_comp()
	test_find_euler()


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


if __name__ == '__main__':
	main()