import csv

class adjacencyList:
    lisst = dict()
    def __init__(self,pathFile):
        i = 0
        with open(str(pathFile),"r") as f:
            for row in csv.reader(f):
                edges = dict()
                x = 0
                for item in row:
                    if(int(item)>0):
                        edges[x] = int(item)
                    x = x+1
                self.lisst[i] = edges
                i = i+1




    def printAdjList(self):
        for i in range(len(self.lisst)):
            print self.lisst.values()[i]
