from random import randint
from itertools import cycle, islice
from math import sqrt

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class DiGraph:

    def __init__(self, num_layers: int):
        self.num_layers = num_layers

        # Create layers
        self.layers = create_layers(num_layers)
        self.vertices_layers = create_vertices_layers(self.layers)
        self.size = sum(self.layers)
        self.adj = np.zeros((self.size, self.size), dtype=int)

        print(self.vertices_layers)

        # Link consequent vertices through random permutations
        for i, layer in enumerate(self.vertices_layers[1:-1]):
            layercp = np.random.permutation([j % len(self.vertices_layers[i]) for j in range(max(len(layer), len(self.vertices_layers[i])))])
            repeated = list(islice(cycle(self.vertices_layers[i+1]), len(layercp)))
            for vx, d in zip(layercp, repeated):
                self.adj[self.vertices_layers[i][vx], d] = 1
        # Manually link last layer
        for v in self.vertices_layers[-2]:
            self.adj[v, self.vertices_layers[-1][0]] = 1

        # Add 2N edges randomly
        for i in range(2*num_layers):
            while True:
                i, j = randint(1, self.size-2), randint(1, self.size-2)
                if self.adj[i,j] == 0:
                    self.adj[i,j] = 1
                    break

        self.adj = np.vectorize(lambda x: randint(1, 10) if x == 1 else 0)(self.adj)
        print(self.adj)

    def show(self):
        graph = nx.from_numpy_matrix(self.adj, create_using=nx.DiGraph)
        pos = nx.spring_layout(graph, iterations=100)

        distance_x = 2/len(self.vertices_layers)
        current_x = -1

        # Calculate the biggest number of vertices in a layer (make even if necessary)
        distance_y = 2/max([len(x) if len(x) % 2 == 0 else len(x) - 1 for x in self.vertices_layers])

        for layer in self.vertices_layers:
            length = len(layer) // 2 if len(layer) > 1 else 1
            positions = np.linspace(-distance_y*length, distance_y*length, len(layer)) if len(layer) > 1 else [0.]
            for i, node in enumerate(layer):
                pos[node][0] = current_x
                pos[node][1] = positions[i]
            current_x += distance_x
        plt.subplot(111)
        # Add scaling of size depending on node quantity
        scaling_factor = 0.5*sqrt(800/(self.size*self.size))
        print("Font size", (12*scaling_factor))
        labels = nx.get_edge_attributes(graph,'weight')
        nx.draw(graph, pos, with_labels=True, font_size=8, node_size=1000*scaling_factor, node_color='#a1b56c')
        nx.draw_networkx_edge_labels(graph, pos, font_size=6, edge_labels=labels)
        plt.show()

    def __str__(self):
        s = '\n'
        for row in self.adj:
            s += ' '.join(str(i) if i > 9 else ' '+str(i) for i in row)
            s += '\n'
        return s


# Create list that specifies number of vertices in each layer
def create_layers(N: int):
    layers = [1]
    for i in range(N):
        layers.append(randint(2, N))
    layers.append(1)
    return layers


# Create list of lists containing vertices numbers in each layer
def create_vertices_layers(layers):
    current_vertex = 0
    vertices = [[] for i in range(len(layers))]
    for layer, num_vert in enumerate(layers):
        for i in range(num_vert):
            vertices[layer].append(current_vertex)
            current_vertex += 1
    return vertices
