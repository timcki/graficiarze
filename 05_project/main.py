import click

from ford_fulkerson import ford_fulkerson
from graph import DiGraph


@click.command()
@click.option('-N', '--num-layers', 'layers', type=int, help='Number of layers in the randomly generated digraph')
def main(layers):
    g = DiGraph(layers)
    print(g)
    print("Maksymalny przeplyw: ", ford_fulkerson(g.adj, 0, len(g.adj[0])-1))
    g.show()
    G = [
        [0, 10, 9, 0, 0, 0],
        [0, 0, 6, 5, 0, 0],
        [0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 9],
        [0, 4, 0, 2, 0, 7],
        [0, 0, 0, 0, 0, 0]
    ]
    print('Maksymalny przepływ: ', ford_fulkerson(G, 0, 5))

    G2 = [
        [0, 10, 4, 0, 0, 0],
        [0, 0, 2, 7, 0, 0],
        [0, 0, 0, 0, 10, 0],
        [0, 0, 4, 0, 3, 2],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0]
    ]
    print('Maksymalny przepływ: ', ford_fulkerson(G2, 0, 5))


if __name__ == '__main__':
    main()