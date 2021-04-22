import random
from components import Components 

def main():
	tries = 200
	su = 0
	for i in range(tries):
		el = [random.randint(0, 6) for x in range(10)]
		su += int(check_seq(el))
	print(su/tries)

	check_comp()


def check_seq(seq):
	if sum(seq) % 2:
		return False
	return True

def check_comp():
	G = [[2, 5], [4], [0, 5], [], [1], [0, 2]]
	components = Components()
	[comp, nr] = components.FindComponents(G)

	compLists = [[] for x in range(nr)]
	for v in range(len(G)):
		compLists[comp[v] - 1].append(v)

	for count, item in enumerate(compLists):
		print(count + 1, item)
	print("Biggest connected component: " + str(components.MaxComponent))
	print("has " + str(components.MaxCountComponents) + " vertices")




if __name__ == '__main__':
	main()