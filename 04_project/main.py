from graph import Graph


def print_adj_list(adj_list):
    for k, v in adj_list:
        print(f"{k}: {v}")

if __name__ == '__main__':
    g = Graph(7)
    g.random_digraph(0.3)
    print(g)
    print_adj_list(g.adj_list.items())
    g.show()
