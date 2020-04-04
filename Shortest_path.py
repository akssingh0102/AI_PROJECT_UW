import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print "Vertex tDistance from Source"
        for node in range(self.V): 
            print node, "t", dist[node] 
