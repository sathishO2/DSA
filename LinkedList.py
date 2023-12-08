class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self,value):
        nnode = node(value)
        self.head = nnode
        self.tail = nnode
        self.length = 1

    def append(self,value):
        nnode = node(value)
        if self.length == 0:
            self.head = nnode
            self.tail = nnode
        else:
            self.tail.next = nnode
            self.tail = nnode
        self.length+=1

    def prepend(self,value):
        nnode = node(value)
        if self.length == 0:
            self.head = nnode
            self.tail = nnode
        else:
            nnode.next = self.head 
            self.head = nnode
        self.length+=1
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def popleft(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            # self.head = None
            self.tail = None
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        nnode = node(value)
        temp = self.get(index-1)
        nnode.next = temp.next
        temp.next = nnode
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>= self.length:
            return None
        if index == 0:
            return self.popleft()
        if index == self.length-1:
            return self.pop()
        
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length-=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def show(self):
        temp = self.head
        while temp:
            print(temp.value,end=" ")
            temp = temp.next


ll = linkedList(1)
ll.append(2)
ll.append(3)
# ll.append(4)
# ll.prepend(0)

# print(ll.pop())
# print(ll.pop())
# print(ll.pop())

# print(ll.popleft())
# print(ll.popleft())
# print(ll.popleft())

# print(ll.get(1))

# print(ll.set(0,99))

# print(ll.insert(2,90))
# print(ll.insert(0,6543))
# print(ll.insert(1,32))

# print(ll.remove(0))
# print(ll.remove(0))

#ll.reverse()

ll.show()