from pyhypergraph import *

def test_reduce_hypergraph():
    h = Hypergraph([0, 1, 2, 3], [{0, 1, 2}, {0, 1}, {0, 2, 3}, {2, 3}])
    
    h_reduced = reduce_hypergraph(h)

    assert h_reduced.vertices == h.vertices
    assert h_reduced.edges == [{0, 1, 2}, {0, 2, 3}]

h = Hypergraph([0,1,2,3,4],[[0,1,2],[0,1],[0,2,3],[2,3]])
print(f"Vertices: {h.vertices} \n Edges: {h.edges} \n Order: {h.order} \n Size: {h.size}")