
class Hypergraph:
    def __init__(self, vertices, edges):
        self._vertices = vertices
        self._edges = edges

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

def reduce_hypergraph(h: Hypergraph) -> Hypergraph:
    edges_reduced = h.edges.copy()

    for i in h.edges:
        for j in h.edges:
            if i == j or not j.issubset(i):
                continue

            edges_reduced.remove(j)

    return Hypergraph(h.vertices.copy(), edges_reduced)
