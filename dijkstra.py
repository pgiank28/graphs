import readGraph
import adjacencyList

class dijkstra:
    def __init__(self,startingPoint):
        self.graph = readGraph.adjList
        self.dist = [10000]*len(self.graph.lisst)
        self.priority_queue = [dict({startingPoint:0})]
        self.dist[startingPoint] = 0

    def printG(self):
        self.graph.printAdjList()

    def accessNode(self,node):
        for key,weight in self.graph.lisst[node].items():
            if self.dist[key] > self.dist[node] + weight:
                self.dist[key] = self.dist[node] + weight
            self.priority_queue.append(dict({key:self.dist[node] + weight}))

    def checkLazyNode(self,node):
        if node.values()[0] > self.dist[node.keys()[0]]:
            return 1
        else:
            return 0

    def lazyDijkstra(self):
        while self.priority_queue:
            node = self.priority_queue.pop(0)
            if self.checkLazyNode(node) == 1:
                continue
            self.accessNode(node.keys()[0])

if __name__ == '__main__':
    df = dijkstra(0)
    df.lazyDijkstra()
    print df.dist
