import readGraph

mat = readGraph.adjMatrix
lis = readGraph.adjList
visited = [0]*len(lis.lisst)
pre = [0]*len(lis.lisst)
post = [0]*len(lis.lisst)
L=[]
topologicalOrder=[]

def explore(node):
    if(visited[node] == 1):
        return
    visited[node] = 1
    print "visited node "+str(node)

    for key in lis.lisst[node].keys():
        explore(key)

    topologicalOrder.append(node)


def depthFirstSearch():
    for i in range(len(visited)):
        explore(i)




def breadthFirstSearch():
    for i in range(len(visited)):
        queue=[]
        queue.append(i)
        while queue:
            node = queue.pop(0)
            if visited[node]==1:
                continue
            visited[node] = 1
            print "visited node  "+str(node)
            for i in lis.lisst[node]:
                queue.append(i)


    return -1

def findCirclesDFS(node,clock):
    if(visited[node] == 1):
        if(clock>pre[node]):
            print "find circle"
            return
        return
    visited[node] = 1;
    pre[node] = clock
    for key in lis.lisst[node].keys():
        findCirclesDFS(key,clock+1)


def findCircles(node,clock):
    if(visited[node] == 1):
        if(clock>pre[node]):
            print "find circle"
            return 1
        return 0
    visited[node] = 1;
    pre[node] = clock
    for key in lis.lisst[node].keys():
        if(findCircles(key,clock+1)==1):
            return 1
    return 0

def kosaraju(node):
    if(visited[node] == 1):
        return
    visited[node] = 1
    L.append(node)
    for key in lis.lisst[node].keys():
        kosaraju(key)


def stronglyConnectedComponentsKosaraju(node):

    for i in range(len(visited)):
        kosaraju(i)

def topologicalSort():
    if(findCircles(0,0)==1):
        print "can't apply topological sort to graphs with circles"
        return


#breadthFirstSearch()
#depthFirstSearch()
#findCyclesDFS(0,0)
#stronglyConnectedComponentsKosaraju(0)
#topologicalSort()
#topologicalSort()
explore(0)
print topologicalOrder[::-1]
