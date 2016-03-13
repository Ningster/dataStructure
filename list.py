from node import Node

class linkedList():
    def __init__(self):
        self.first = None
        self.last = None
    def addNode(self, nodeID, weight):
        if self.first == None:
            self.first = Node(nodeID, weight)
            self.last=self.first
        else:
            self.last.next = Node(nodeID, weight)
            self.last = self.last.next
    def printLinkedList(self):
        current = None
        if self.first != None:
            self.first.printNode()
            current=self.first.next
            while current != None:
                current.printNode()
                current=current.next
    def getMinNode(self):
        if self.first==None or self.last == None:
            return None
        elif self.first == self.last:
            return self.first
        else:
            minNode= self.first
            currentNode = self.first.next
            while currentNode.weight < minNode.weight:
                minNode = currentNode
                currentNode = currentNode.next
            return minNode
