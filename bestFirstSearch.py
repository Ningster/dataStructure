from heapq import *

weightMatrix = [
              [0,1,3,2,(),(),(),()],
              [(),0,(),(),5,(),3,()],
              [(),(),0,(),4,3,(),()],
              [(),(),(),0,(),2,7,()],
              [(),(),(),(),0,(),(),4],
              [(),(),(),(),(),0,(),1],
              [(),(),(),(),(),(),0,1],
              [(),(),(),(),(),(),(),0]
              ]

class heapNode():
    def __init__(self, id):
        self.id = id
        self.visitList=[]
        self.accWeight=0


def createChildNode(weightMatrix,currentNode,id):
    childNode=heapNode(id)
    childNode.visitList=currentNode.visitList + [currentNode.id]
    childNode.accWeight=weightMatrix[currentNode.id][id]+currentNode.accWeight
    return childNode

def bestFirstSearch(n,weightMatrix,dest): #n points
    h = [] #Initialize heap
    B = () #Initialize bound
    rootNode=heapNode(0) #Initialize rootNode
    heappush(h,(rootNode.accWeight,rootNode)) #push rootNode into the heap
    while h:                #when heap is not empty
        currentNode = heappop(h)[1]   #pop out the node with the smallest weight
        if currentNode.accWeight < B: #if it's a possible node
            for i in range(0,n):           #expand its children
                if weightMatrix[currentNode.id][i] is not () and weightMatrix[currentNode.id][i] is not 0:
                    childNode = createChildNode(weightMatrix,currentNode,i)
                    print childNode.visitList,childNode.id
                    heappush(h,(childNode.accWeight,childNode))
                    if childNode.id == dest:  #if the child is destination, update bound and path
                        B = childNode.accWeight
                        path = childNode.visitList+[childNode.id]
    return B,path

print bestFirstSearch(8,weightMatrix,7)
