class DisjointSet:
    def __init__(self,nodes = 0):
        self.size = [1]*(nodes+1)
        self.parent = [i for i in range(nodes+1)]

    def findUltimatePar(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUltimatePar(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        uParent = self.findUltimatePar(u)
        vParent = self.findUltimatePar(v)
        if uParent == vParent:
            return
        if self.size[uParent] <= self.size[vParent]:
            self.parent[vParent] = uParent
            self.size[uParent] += self.size[vParent]
        else:
            self.parent[uParent] = vParent
            self.size[vParent] += self.size[uParent]

root = DisjointSet(7)
root.unionBySize(1,2)
root.unionBySize(2,3)
root.unionBySize(4,5)
root.unionBySize(6,7)
root.unionBySize(5,6)
if root.findUltimatePar(3) == root.findUltimatePar(7):
    print("3 and 7 are connected\n")
else:
    print( "3 and 7 are not connected\n")  
  
root.unionBySize(3,7)  
if root.findUltimatePar(3) == root.findUltimatePar(7):
    print("3 and 7 are connected\n")
else:
    print( "3 and 7 are not connected\n") 
