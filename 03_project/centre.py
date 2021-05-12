import numpy as np
from dijkstra import *

def make_distance_matrix(G):
    matrix = np.zeros(shape=G.adj.shape)

    for row in range(0, len(matrix[0])):
        D = Dijkstra()
        D.do_dijkstra(G.adj, G.adj, row+1)
        matrix[row, :] = D.ds
        pass

def get_center(distance_matrix):
    center = np.argmin(np.sum(distance_matrix, axis=0)) + 1
    return center

def get_minimax_center(distance_matrix):
    minimax_center = np.argmin(np.max(distance_matrix, axis=0)) + 1
    return minimax_center