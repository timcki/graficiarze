import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from components import Components
from dijkstra import Dijkstra
from centre import *

class Graph:
    def __init__(self, n, prob):
        self.prob = prob
        self.n = n
        self.adj = np.zeros((n, n), dtype=int)
        self.biggest_comp = []

    def rand_graph(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                self.adj[i, j] = self.adj[j, i] = int(random.uniform(0, 1) <= self.prob)

    def choose_biggest_comp(self):
        adjacency = self.adj.tolist()
        components = Components()
        [comp, nr] = components.find_components(adjacency)

        for v in range(self.n):
            if comp[v] == components.max_component:
                self.biggest_comp.append(v)
        for i in reversed(range(self.n)):
            if i not in self.biggest_comp:
                adjacency.pop(i)
            else:
                for j in reversed(range(self.n)):
                    if j not in self.biggest_comp:
                        adjacency[i].pop(j)
        
        self.n -= (self.n - len(self.biggest_comp))
        self.adj = np.array(adjacency)

    def assign_weights(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.adj[i, j] != 0:
                    self.adj[i, j] = self.adj[j, i] = random.randint(1, 10)

    def __str__(self):
        s = ""
        for row in self.adj:
            s += " ".join(str(i) if i > 9 else str(i)+' ' for i in row)
            s += '\n'
        return s

