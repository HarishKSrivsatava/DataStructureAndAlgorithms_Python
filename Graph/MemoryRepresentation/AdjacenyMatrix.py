
"""
    Sample Graph :
                 a --------b
                /          \
               /            \
              c--------------d -----------e
"""

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    # Get the vertices of Graph
    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findEdges()

    def findEdges(self):
        edges = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edges :
                    edges.append({nxtvrtx, vrtx})
        return edges

    def addVertex(self,vrxt):
        if vrxt not in self.gdict:
            self.gdict[vrxt] = []

    def addEdge(self,edge):
        print("Edge ", edge)
        edge = set(edge)
        print("Set Edge", edge)
        (vrtx1, vrtx2) = tuple(edge)
        print("Tuple ", tuple(edge))
        print("vrtx1 ", vrtx1)
        print("vrtx2 ", vrtx2)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]



# Driver Code
graph_elements = {
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["b","c","e"],
    "e" : ["d"]
                }
g = graph(graph_elements)
print(g.getVertices())
print(g.edges())

# adding a vertex in graph
g.addVertex("f")
print(g.getVertices())

g.addEdge({'b','e'})

"""
    Sample Graph :
                 a ----------------b
                /                 /  \
               /                 /    \
              c-----------------d -----e
"""
print(g.edges())