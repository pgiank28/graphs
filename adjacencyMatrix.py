from turtle import *
import csv

class adjacencyMatrix:
    matrix = list()
    def __init__(self,pathFile):
        with open(str(pathFile),"r") as f:
            self.matrix = list(csv.reader(f))
        f.close()
        
    def printAdjMatrix(self):
        for line in self.matrix:
            print(line)

    def graphAdjMatrix(self):
        color('red', 'yellow')
        begin_fill()
        for line in self.matrix:
            pendown()
            self.makeCircle()
            penup()
            setx(10)
            sety(10)
            if abs(pos()) < 1:
                break
        end_fill()
        done()

    def makeCircle(self):
        forward(2)
        right(13)
        forward(24)
        right(56)
        forward(44)
