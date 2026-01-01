
class Hypergraph:
    def __init__(self, vertices: list, edges: list):
        self._vertices = vertices
        self._edges = edges

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges
    
    #The following two methods will return the order and cardinality of the hypergraph

    @property
    def order(self):
        return len(self._vertices)
    
    @property
    def size(self):
        return len(self._edges)

def reduce_hypergraph(h: Hypergraph) -> Hypergraph:
    edges_reduced = h.edges.copy()

    for i in h.edges:
        for j in h.edges:
            if i == j or not j.issubset(i):
                continue

            edges_reduced.remove(j)

    return Hypergraph(h.vertices.copy(), edges_reduced)
