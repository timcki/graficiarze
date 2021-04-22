class Components():
    max_component = 1
    max_count = 0
    count = 0
    def find_components(self, G):
        nr = 0
        comp = []
        for v in range(len(G)):
            comp.append(-1)
        for v in range(len(G)):
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                self.one_component(nr, v, G, comp)
                if self.max_count < self.count:
                    self.max_count = self.count
                    self.max_component = nr
                self.count = 0
        return [comp, nr]

    def one_component(self, nr, v, G, comp):
        self.count += 1
        for u in range(len(G[v])):
            if G[v][u] == 1 and comp[u] == -1:
                comp[u] = nr
                self.one_component(nr, u, G, comp)
