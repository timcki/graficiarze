class Components():
    MaxComponent = 1
    MaxCountComponents = 0
    CountComponents = 0
    def FindComponents(self, G):
        nr = 0
        comp = []
        for v in range(len(G)):
            comp.append(-1)
        for v in range(len(G)):
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                self.OneComponent(nr, v, G, comp)
                if self.MaxCountComponents < self.CountComponents:
                    self.MaxCountComponents = self.CountComponents
                    self.MaxComponent = nr
                self.CountComponents = 0
        return [comp, nr]

    def OneComponent(self, nr, v, G, comp):
        self.CountComponents += 1
        for u in G[v]:
            if comp[u] == -1:
                comp[u] = nr
                self.OneComponent(nr, u, G, comp)
