# Bellman Ford Algorithm
# Relax edges and search through the whole grap
# Based on lesson and examples from Neelam Yadav and Himanshu Garg
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

import time
from timeit import default_timer as timer

class Graph:
    #Initialize and make graph and vertices list
    def __init__(self, vertices):
        self.graphVertex = vertices  
        self.graph = []
 
    #new representation rather than adjacency matrix
    def addEdge(self, u, v, w):

        self.graph.append([u, v, w])

    def printArray(self, dist):

        for i in range(self.graphVertex):
            print("{0}\t\t{1}".format(i, dist[i]))
 
    #Explore using bellmanFord
    def BellmanFord(self, sourceVertex):
 
        dist = [float("Infinity")] * self.graphVertex
        dist[sourceVertex] = 0
 

        for _ in range(self.graphVertex - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Infinity") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
 

 
        for u, v, w in self.graph:
            if dist[u] != float("Infinity") and dist[u] + w < dist[v]:
                print("Negative weight cycles")
                return
 
        # print all distance
        #self.printArray(dist)
 
 
# Add all edges that are the same as our Dijkstra's example
if __name__ == '__main__':
    g = Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 7, 11)
    g.addEdge(3, 2, 7)
    g.addEdge(2, 5, 4)
    g.addEdge(2, 8, 2)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
    # function call


sum = 0

for i in range(10):
    start = float(timer())
    g.BellmanFord(0)
    end = float(timer())
    sum = sum + (end-start)

print(sum)
