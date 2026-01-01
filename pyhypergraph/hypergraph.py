
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
    
    #The following two methods will return the order and size of the hypergraph

    @property
    def order(self):
        return len(self._vertices)
    
    @property
    def size(self):
        return len(self._edges)
    
    #Tells python how to represent a hypergraph
    def __repr__(self):
        return f"Hypergraph({self.vertices},{self.edges})"

def reduce_hypergraph(h: Hypergraph) -> Hypergraph:
    edges_reduced = h.edges.copy()

    for i in h.edges:
        for j in h.edges:
            if i == j or not j.issubset(i):
                continue

            edges_reduced.remove(j)

    return Hypergraph(h.vertices.copy(), edges_reduced)

#function to find all the incident edges of a vertex.
def star_center_at(h:Hypergraph, vertex) -> list:
    
    """
    Docstring for star_center_at
        (hypergraph,any) -> list

        This function takes a vertex v and hypergraph h and returns a list of all the edges e in h that contain v
        i.e. return all the incident edges of v.

        Example

        h = Hypergraph([1,2,3,4,5],[[1,2,3],[1,2,5],[3,4]])
        print(star_center_at(h,3))

        >>> [[1,2,3],[3,4]]
    
    """

    if vertex not in h.vertices:
        raise ValueError(f"'{vertex}' is not a vertex of the {h}")
    
    incident_edges = []
    for e in h.edges:
        if vertex in e:
            incident_edges.append(e)

    return incident_edges
