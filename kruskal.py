class graph():
    def __init__(self,n): #Initialize graph to an empty two-dimensional array based on given n
        self.graph = [['' for i in range(0,n)]for i in range(0,n)]
        self.n=n
    def addVEW(self,f,t,w): #Add weight into the array
        self.graph[f][t]=w
        self.graph[t][f]=w
    def addInf(self): #Add infinity for unreachable vertices
        n = self.n
        for i in range(0,n):
            d = 0
            while i!=d:
                if self.graph[i][d]=='':
                    self.addVEW(i,d,())
                d=d+1
    def getGraph(self):
        return self.graph
    def heapArray(self):  #Construct an array to store all edges.
        result = [0]
        n = self.n
        for i in range(0,n):
            d = 0
            while i!=d:
                result.append([i,d])
                d=d+1
        return result
    def getHeapSize(self): #Get the size of the heapArray
        n=self.n
        return n*(n-1)/2
    def getWeight(self,a): #Get the weight of the edge.
        f=a[0]
        t=a[1]
        return self.graph[f][t]

def adjust(a,i,n,g):  #a is a heapArray, n is heapSize
    item = a[i]
    j = 2*i
    while j<=n:
        if j<n and g.getWeight(a[j])>g.getWeight(a[j+1]): #to find the smaller son
            j = j+1
        if g.getWeight(item)<=g.getWeight(a[j]):  #the position for the item is found
            break
        else:
            a[j/2]=a[j]
            j = 2*j
    a[j/2]=item


def heapify(a,n,g):
    for i in range(n/2,0,-1):
        adjust(a,i,n,g)

def findRoot(p,i):
    while p[i]>=0:
        i = p[i]
    return i

def union(p,f,t):
    fR = findRoot(p,f)
    tR = findRoot(p,t)
    if p[fR]<p[tR]:
        p[fR]=p[fR]+p[tR]
        p[tR]=fR
    else:
        p[tR]=p[tR]+p[fR]
        p[fR]=tR

def isNotCycle(p,a): #p is parent array, a is input array
    f = a[0]
    t = a[1]
    if findRoot(p,f)!=findRoot(p,t):
        union(p,f,t)
        return True
    else:
        return False

def swap(A,c,d):
    temp = A[c]
    A[c]=A[d]
    A[d]=temp


def kruskal(g):  #g is a graph
    cost = 0
    T = []
    n = g.n  #number of verticies
    i = 0
    A = g.heapArray()
    N = g.getHeapSize()
    p = [-1 for j in range(0,n)] #Initialize a disjoint set
    heapify(A,N,g)
    while i<n-1:
        if isNotCycle(p,A[1]):
            T.append(A[1])
            cost = cost+g.getWeight(A[1])
            i=i+1
        swap(A,1,N)
        N = N-1
        adjust(A,1,N,g)
    return cost, T

g=graph(6)
g.addVEW(0,0,0)
g.addVEW(1,1,0)
g.addVEW(2,2,0)
g.addVEW(3,3,0)
g.addVEW(4,4,0)
g.addVEW(5,5,0)
g.addVEW(0,1,10)
g.addVEW(0,4,45)
g.addVEW(0,3,30)
g.addVEW(1,2,50)
g.addVEW(1,4,40)
g.addVEW(1,5,25)
g.addVEW(2,4,35)
g.addVEW(2,5,15)
g.addVEW(3,5,20)
g.addVEW(4,5,55)
g.addInf()

g2=graph(10)
g2.addVEW(0,0,0)
g2.addVEW(1,1,0)
g2.addVEW(2,2,0)
g2.addVEW(3,3,0)
g2.addVEW(4,4,0)
g2.addVEW(5,5,0)
g2.addVEW(6,6,0)
g2.addVEW(7,7,0)
g2.addVEW(8,8,0)
g2.addVEW(9,9,0)
g2.addVEW(0,1,7)
g2.addVEW(0,7,10)
g2.addVEW(1,2,5)
g2.addVEW(1,8,3)
g2.addVEW(1,6,6)
g2.addVEW(2,3,1)
g2.addVEW(2,8,9)
g2.addVEW(3,4,4)
g2.addVEW(3,9,7)
g2.addVEW(4,5,2)
g2.addVEW(5,9,1)
g2.addVEW(5,6,8)
g2.addVEW(6,8,8)
g2.addVEW(6,7,10)
g2.addVEW(8,9,6)
g2.addInf()

print kruskal(g)    #(105, [[1, 0], [5, 2], [5, 3], [5, 1], [4, 2]])
print kruskal(g2)   #(39, [[9, 5], [3, 2], [5, 4], [8, 1], [4, 3], [2, 1], [6, 1], [1, 0], [7, 0]])
