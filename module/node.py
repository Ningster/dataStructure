class Node():
    def __init__(self, nodeID, weight):
        self.id = nodeID
        self.weight = weight
        self.next = None
    def printNode(self):
            print str(self.id) + ': '+str(self.weight) #+' '+ self.get_next_id()
