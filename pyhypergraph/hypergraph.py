import random

class Hypergraph:
    def __init__(self, vertices: list = [], edges: list = []):
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
    
    #Determines if a hypergraph is empty
    def is_empty(self):
        """
        Docstring for is_empty
        
        () -> bool
        determine if a hypergraph is empty or not i.e. if the hypergraph has no edges nor vertices.

        Example
        h = Hypergraph([],[])
        print(h.is_empty())

        >>> True

        """

        return not self.vertices and not self.edges
    
    #Determines if a hypergraph is trivial
    def is_trivial(self):
        """
        Docstring for is_trivial
        
        () -> bool
        determine if a hypergraph is trivial i.e. if the hypergraph has no edges but has vertices.

        Example
        h = Hypergraph([1],[])
        print(h.is_trivial())

        >>> True

        """

        return not not self.vertices and not self.edges
    
    #deletes a vertec from hypergraph
    def weak_vertex_deletion(self,vertex):

        """
        Docstring for weak_vertex_deletion
        
        (any) -> None

        This method deletes a vertex from the hypergraph

        Note: it does not return anything and it directly modifies the hypergraph.
            - if you want to use this method and still have the original hypergraph, make sure you have a copy of the original.
        
        Example

        h = Hypergraph([1,2,3,4,5],[[1,2,3],[1,2,5],[3,4]])
        h.weak_vertex_deletion(3)
        print(h)

        >>> Hypergraph([1, 2, 4, 5],[[1, 2], [1, 2, 5], [4]])
            
        """
        
        if vertex in self.vertices:
            self.vertices.remove(vertex)

            for e in self.edges:
                if vertex in e:
                    e.remove(vertex)
        else:
            print(f"{vertex} is not a vertex of {self}")
    
    #deletes an edge from hypergraph
    def weak_edge_deletion(self, edge: list):
        """
        Docstring for weak_edge_deletion
        
        (list) -> None

        This method deletes the edge from the hypergraph while leaving the vertices unchange

         Note: it does not return anything and it directly modifies the hypergraph.
            - if you want to use this method and still have the original hypergraph, make sure you have a copy of the original.

        Example

        h = Hypergraph([1,2,3,4,5],[[1,2,3],[1,2,5],[3,4]])
        h.weak_edge_deletion([1,2,3])
        print(h)

        >>> Hypergraph([1, 2, 3, 4, 5],[[1, 2, 5], [3, 4]])
        """
        if edge in self.edges:
            self.edges.remove(edge)
        else:
            print(f"{edge} is not a hyperedge of {self}")

    #deletes a vertex and all its incident edges from hypergraph
    def strong_vertex_deletion(self,vertex):
        """
        Docstring for strong_vertex_deletion
        
        (any) -> None

        This method deletes a vertex and all its incident edges from the hypergraph

        Note: it does not return anything and it directly modifies the hypergraph.
            - if you want to use this method and still have the original hypergraph, make sure you have a copy of the original.
        
        Example

        h = Hypergraph([1,2,3,4,5],[[1,2,3],[1,2,5],[3,4]])
        h.strong_vertex_deletion(3)
        print(h)

        >>> Hypergraph([1, 2, 4, 5],[[1, 2, 5]])

        """
        if vertex in self.vertices:

            self.vertices.remove(vertex)

            for e in self.edges:
                if vertex in e:
                    self.edges.remove(e)
        else:
            print(f"{vertex} is not a vertex of {self}")

    #deletes an edge and all its vertices from the hypergraph
    def strong_edge_deletion(self,edge:list):
        """
        Docstring for strong_edge_deletion
        
        (list) -> None

        This method deletes the edge and all the vertices in it from the hypergraph 

         Note: it does not return anything and it directly modifies the hypergraph.
            - if you want to use this method and still have the original hypergraph, make sure you have a copy of the original.

        Example

        h = Hypergraph([1,2,3,4,5],[[1,2,3],[1,2,5],[3,4]])
        h.strong_edge_deletion([1,2,3])
        print(h)

        >>> Hypergraph([4, 5],[[5], [4]])
        """
        if edge in self.edges:

            self.edges.remove(edge)

            for vertex in edge:
                self.weak_vertex_deletion(vertex)
        
        else:

            print(f"{edge} is not a hyperedge of {self}")

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

#Hypergraph greedy coloring algorithm
def coloring(h: Hypergraph) -> list:

    """
    Docstring for coloring
    
    (Hypergraph) -> list

    This function takes in a hypergraph as parameter and color the vertices of the graph such that no edge (that is not
    a loop) contains only one color (i.e is monochromatic).

    The algorithm works by taking the vertices, and for each vertex, we determine to which coloring partitions it can be added
    without an edge been monochromatic; then we take the first coloring partition that fits and we insert the vertex there.

    To determine which partition is not valid for a given vertex, we simply check if by removing the vertex from its incident edges, 
    the edges become monochromatic. If it becomes monochromatic we know that the given color partition is not a valid and we can exclude
    it from the list of given partition.

    if no valid partition is found after verifying which coloring partition can fit the vertex, we just create a new one with the vertex
    as first entry. 

    Note: The algorithm used is greedy as such it may not always return the optimal solution if the other is not correct.
    - To give the algorithm a chance to return the optimal solution, the vertices are shuffled.
    - Also when refering to color_partition, I mean a list of vertices that are colored the same.
    """

    coloring_partition = []

    if h.is_empty():
        return coloring_partition
    
    coloring_partition.append([])

    #shuffle the vertices for the greedy algorithm
    shuffled_vertices = h.vertices
    random.shuffle(shuffled_vertices)

    for  v in shuffled_vertices:
    
        forbidden_partition = [] #list of partition that cannot take v without an edge been monochromatics

        for e in star_center_at(h,v):

            e_without_v = [ x for x in e if x != v ] #removing v from its incident esges

            if not e_without_v: #skip if the edge is a loop
                continue

            for c in coloring_partition:
                if set(e_without_v).issubset(set(c)): #verify if an edge is almost monochromatic (i.e lacks v to be colored the same as the other vertices to become monochromatic)
                    forbidden_partition.append(c) #adds the partition as invalid partition for vertex v

        available_partition = [x for x in coloring_partition if x not in forbidden_partition] #finds all the partition that can take v without any edge be monochromatic

        if not available_partition: #create a new partition if v can't be fitted in any partition without an edge been monochromatic
            coloring_partition.append([v])
        else: #adds v to the first partition where it fits.
            coloring_partition[coloring_partition.index(available_partition[0])].append(v)

    return coloring_partition