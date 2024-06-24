class Node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

def buildTree(s,e):
    #base condition
    if s == e:
        temp = Node()
        temp.val = arr[s]
        return temp
    if s > e:
        return None
    mid = s+(e-s)//2
    temp = Node()
    temp.val = arr[mid]
    l = buildTree(s,mid-1)
    r = buildTree(mid+1,e)
    temp.left = l
    temp.right = r
    return temp

def findHeight(node):
    if node == None:
        return 0
    l = findHeight(node.left)
    r = findHeight(node.right)
    return max(l,r)+1

arr = [1,2,3,4,5,6,7]
root = buildTree(0,len(arr)-1)
height = findHeight(root)
print(height)


