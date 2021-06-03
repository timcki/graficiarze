class Dijkstra():
    def init(self, G, s):
        self.ds = [1000000 for v in range(len(G))]
        self.ps = [-1 for v in range(len(G))]
        self.ds[s] = 0

    def relax(self, u, v, w):
        if self.ds[v] > self.ds[u] + w[u][v]:
            self.ds[v] = self.ds[u] + w[u][v]
            self.ps[v] = u

    def do_dijkstra(self, G, w, s):
        self.init(G, s)
        S = []
        while len(S) != len(G):
            for v in range(len(G)):
                if v not in S:
                    min = v
                    break
            for v in range(len(G)):
                if v not in S:
                    if self.ds[min] > self.ds[v]:
                        min = v

            S.append(min)
            for v in range(len(G)):
                if G[v][min] != 0 and v not in S:
                    self.relax(min, v, w)
