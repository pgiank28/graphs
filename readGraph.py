import sys
import adjacencyMatrix as am
import adjacencyList as al

if(len(sys.argv) < 2):
    print "You must input the path of the file containing the graph"
    sys.exit()


adjMatrix = am.adjacencyMatrix(sys.argv[1])
adjList = al.adjacencyList(sys.argv[1])
