class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        nnode = node(value)
        if self.root is None:
            self.root = nnode
            return True
        temp = self.root
        while(True):
            if temp.value == value:
                return False
            if temp.value > value:
                if temp.left is None:
                    temp.left = nnode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = nnode
                    return True
                temp = temp.right

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value<value:
                temp = temp.right
            else:
                return True
        return False
            


bst = BinarySearchTree()

bst.insert(2)
bst.insert(3)
bst.insert(1)

print(bst.contains(3))

print(bst.root.right.value)
