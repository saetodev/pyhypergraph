from pyhypergraph.hypergraph import *

def test_reduce_hypergraph():
    h = Hypergraph([0, 1, 2, 3], [{0, 1, 2}, {0, 1}, {0, 2, 3}, {2, 3}])
    
    h_reduced = reduce_hypergraph(h)

    assert h_reduced.vertices == h.vertices
    assert h_reduced.edges == [{0, 1, 2}, {0, 2, 3}]

h = Hypergraph([1,2,3,4,5],[[1,2,3],[1,2,5],[3,4]])
x = Hypergraph([1,2,3])
#print(f"Vertices: {h.vertices} \n Edges: {h.edges} \n Order: {h.order} \n Size: {h.size}")
#print(h.is_empty())
#print(x.is_empty())
#print(x.is_trivial())
#
#print(star_center_at(h,2))

#print(coloring(h))

#h.strong_edge_deletion([1,2,3,4])
#print(h.degree_of(1))

#print(x.is_k_regular())

print(x.is_k_uniform())
print(h)