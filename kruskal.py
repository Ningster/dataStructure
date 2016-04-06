class graph():  #graph in array
    def __init__(self,n):
        self.graph = [['' for i in range(0,n)]for i in range(0,n)]
        self.n=n
    def getGraph(self):
        return self.graph
    def addVEW(self,f,t,w):
        self.graph[f][t]=w
        self.graph[t][f]=w
    def heapArray(self):  #to get every edges in an array for heap
        result = [0]
        n = self.n
        for i in range(0,n):
            d = 0
            while i!=d:
                result.append([i,d])
                d=d+1
        return result
    def getHeapSize(self):
        n=self.n
        return n*(n-1)/2
    def getWeight(self,a):
        f=a[0]
        t=a[1]
        return self.graph[f][t]


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
g.addVEW(0,2,())
g.addVEW(0,5,())
g.addVEW(1,2,50)
g.addVEW(1,4,40)
g.addVEW(1,5,25)
g.addVEW(1,3,())
g.addVEW(2,4,35)
g.addVEW(2,5,15)
g.addVEW(2,3,())
g.addVEW(3,5,20)
g.addVEW(3,4,())
g.addVEW(4,5,55)


def adjust(a,i,n):  #a is a heapArray, n is heapSize
    item = a[i]
    j = 2*i
    while j<=n:
        if j<n and g.getWeight(a[j])>g.getWeight(a[j+1]): #to find the smaller son
            j = j+1
        if g.getWeight(item)<=g.getWeight(a[j]):  #the position for the itme is found
            break
        else:
            a[j/2]=a[j]
            j = 2*j
    a[j/2]=item


def heapify(a,n):  #bottom up
    for i in range(n/2,0,-1):
        adjust(a,i,n)

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
    n = g.n  #vertex number
    i = 0
    A = g.heapArray()
    N = g.getHeapSize()
    p = [-1 for j in range(0,n)]
    heapify(A,N)
    while i<n-1:
        print p
        if isNotCycle(p,A[1]):
            print A[1]
            T.append(A[1])
            cost = cost+g.getWeight(A[1])
            i=i+1
        swap(A,1,N)
        N = N-1
        adjust(A,1,N)
    return cost


print kruskal(g)
