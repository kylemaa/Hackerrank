# a pythonista would always use while queue: instead of while queue != None :
def levelOrder(self,root):
    queue = [root] if root else []
    
    while queue:
        node = queue.pop()
        print(node.data, end=" ")
        
        if node.left: queue.insert(0,node.left)
        if node.right: queue.insert(0,node.right)