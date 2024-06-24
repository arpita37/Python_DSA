class DisjointSet:
    def __init__(self,nodes = 0):
        self.rank = [0]*(nodes+1)
        self.parent = [i for i in range(nodes+1)]

    def findUltimatePar(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUltimatePar(self.parent[node])
        return self.parent[node]

    def unionByRank(self,u,v):
        uParent = self.findUltimatePar(u)
        vParent = self.findUltimatePar(v)
        if uParent == vParent:
            return
        if self.rank[uParent] == self.rank[vParent]:
            self.parent[vParent] = uParent
            self.rank[uParent] += 1
        elif self.rank[uParent] > self.rank[vParent]:
            self.parent[vParent] = uParent
        else:
            self.parent[uParent] = vParent

root = DisjointSet(7)
root.unionByRank(1,2)
root.unionByRank(2,3)
root.unionByRank(4,5)
root.unionByRank(6,7)
root.unionByRank(5,6)
if root.findUltimatePar(3) == root.findUltimatePar(7):
    print("3 and 7 are connected\n")
else:
    print( "3 and 7 are not connected\n")  
  
root.unionByRank(3,7)  
if root.findUltimatePar(3) == root.findUltimatePar(7):
    print("3 and 7 are connected\n")
else:
    print( "3 and 7 are not connected\n") 
