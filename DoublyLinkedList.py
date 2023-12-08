class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        nnode = node(value)
        self.head = nnode
        self.tail = nnode
        self.length = 1
    
    def append(self,value):
        nnode = node(value)
        if self.length==0:
            self.head = nnode
            self.tail = nnode
        else:
            nnode.prev = self.tail
            self.tail.next = nnode
            self.tail = nnode
        self.length+=1
        return True
    
    def prepend(self,value):
        nnode = node(value)
        if self.length == 0:
            self.head = nnode
            self.tail = nnode
        else:
            self.head.prev = nnode
            nnode.next = self.head
            self.head = nnode
        self.length+=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length-=1
        return temp
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp
    
    def get(self,index):
        if index<0 or self.length <= index:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # def get(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #     temp = self.head
    #     if index < self.length/2:
    #         for _ in range(index):
    #             temp = temp.next
    #     else:
    #         temp = self.tail
    #         for _ in range(self.length - 1, index, -1):
    #             temp = temp.prev  
    #     return temp

    def set(self,index,value):
        if index<0 or index >= self.length:
            return False
        temp = self.get(index)
        temp.value = value
        return True
    # def set_value(self, index, value):
    #     temp = self.get(index)
    #     if temp:
    #         temp.value = value
    #         return True
    #     return False

    def insert(self,index,value):
        if index<0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if self.length == index:
            return self.append(value)
        nnode = node(value)
        temp = self.get(index-1)
        nnode.prev = temp
        nnode.next = temp.next
        temp.next.prev = nnode
        temp.next = nnode
        self.length+=1
        return True
    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)

    #     new_node = Node(value)
    #     before = self.get(index - 1)
    #     after = before.next

    #     new_node.prev = before
    #     new_node.next = after
    #     before.next = new_node
    #     after.prev = new_node
        
    #     self.length += 1   
    #     return True  

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length-=1
        return temp


    def show(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
        print()

dll = DoublyLinkedList(1)
dll.append(2);dll.append(3);dll.append(4)

dll.prepend(0)

# dll.pop();dll.pop()

#dll.popfirst();dll.popfirst()

# print(dll.get(0))

# dll.set(4,987)

dll.insert(2,67)
dll.remove(2)

dll.show()