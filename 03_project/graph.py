import random
from components import Components
from dijkstra import Dijkstra

class Graph:
    def __init__(self, n):
        self.prob = 0.5
        self.n = n
        self.adj = [[0 for x in range(self.n)] for y in range(self.n)]
        self.rand_graph()
        self.biggest_comp = []
        self.choose_biggest_comp()
        self.assign_weights()

    def rand_graph(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                self.adj[i][j] = self.adj[j][i] = int(random.uniform(0, 1) <= self.prob)

    def choose_biggest_comp(self):
        components = Components()
        [comp, nr] = components.find_components(self.adj)

        for v in range(self.n):
            if comp[v] == components.max_component:
                self.biggest_comp.append(v)
        for i in reversed(range(self.n)):
            if i not in self.biggest_comp:
                self.adj.pop(i)
            else:
                for j in reversed(range(self.n)):
                    if j not in self.biggest_comp:
                        self.adj[i].pop(j)
        
        self.n -= (self.n - len(self.biggest_comp))

    def assign_weights(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.adj[i][j] != 0:
                    self.adj[i][j] = self.adj[j][i] = random.randint(1, 10)



def main():
    print('Podaj liczbę wierzchołków: ')
    n = int(input())
    G = Graph(n)
    for v in range(G.n):
        print(G.adj[v])

    print(f'Podaj wierzchołek startowy od 0 do {G.n - 1}: ')
    start = int(input())
    D = Dijkstra()
    D.do_dijkstra(G.adj, G.adj, start)

    print("START: s = " + str(start))
    for v in range(G.n):
        print(f'd({v}) = {D.ds[v]} ==> [', end='')
        print_ps(v, D)
        print(']')

def print_ps(v, D):
    if D.ps[v] != -1:
        print_ps(D.ps[v], D) 
        print(' - ', end='')
    print(v, end='')

if __name__ == '__main__':
	main()
        