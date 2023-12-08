# STACK (LIFO)
# class node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class stack:
#     def __init__(self,value):
#         nnode = node(value)
#         self.top = nnode
#         self.length = 1
    
#     def push(self,value):
#         nnode = node(value)
#         if self.length == 0:
#             self.top = nnode
#         else:
#             nnode.next = self.top
#             self.top = nnode
#         self.length+=1
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.top
#         self.top = temp.next
#         temp.next = None

#     def show(self):
#         temp = self.top
#         while temp:
#             print(temp.value,end=" ")
#             temp = temp.next
#         print()

# stk = stack(1)
# stk.push(2)
# stk.push(3)
# stk.push(4)

# stk.pop()
# stk.pop()

# stk.show()


#QUEUE (FIFO)
class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self,value):
        nnode = node(value)
        self.first = nnode
        self.last = nnode
        self.length = 1
    
    def enque(self,value):
        nnode = node(value)
        if self.length == 0:
            self.first = nnode
            self.last = nnode
        else:
            self.last.next = nnode
            self.last = nnode
        self.length+=1
    
    def deque(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        return temp
    
    def show(self):
        temp = self.first
        while temp:
            print(temp.value,end=" ")
            temp = temp.next
        print()

que = Queue(1)
que.enque(2)
que.enque(3)
que.enque(4)

que.deque()
que.deque()

que.show()
    