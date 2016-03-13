from list import linkedList

class Graph():
    def __init__(self):
        self.graph={}
    def addVert(self,name):
        if not name in self.graph:
            self.graph[name]=linkedList()
    def addEdge(self, start, dest, weight):
        if self.graph[start] and self.graph[dest]:
            self.graph[start].addNode(dest, weight)
    def printGraph(self):
        for key in self.graph:
            print 'Graph ['+str(key)+' ]' +' has '
            self.graph[key].printLinkedList()
    def getNode(self,v,n):
        return self.graph[v][n]
    def getMin(self):
        minNode=None
        minV=None
        for v in self.graph:
            if minNode == None:
                minNode = self.graph[v].getMinNode()
            elif self.graph[v].getMinNode().weight < minNode.weight:
                minNode = self.graph[v].getMinNode()
                minV = str(v)
        #return minV,minNode
        return minNode
