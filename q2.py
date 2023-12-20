class LLStack:
    """
    Implements a stack using a singly-linked list.

    Example usage:

      mystack = LLStack()
      mystack.push(3)

    Please note that this implementation is incorrect/incomplete 
    and you are expected to modify it and include it in your 
    submission (see question).
    """

      #mystack.push(3)

    class _Node:
        def __init__(self, element, next):
            self._element = element #Equivalent to get and set methods
            self._next = next

    def __init__(self):
        self._head = None   #equivalent to this keyword in C# - not necessary in c# though.
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):  #Top of the stack is the head of the linked list
        #raise NotImplementedError
        newnode = self._Node(e, self._head) #Creates a new node with the element we pass in and setting the next element to the curret head of the list
        self._head = newnode    #This new node is now the head of the list
        self._size = self._size + 1 # Obviously - the size will increase by 1.


    def top(self):  #Was originally broken when the stack is empty.
        if self.is_empty():
            raise Exception("EmptyStackException")
        else:
            return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception("EmptyStackException")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        return answer

########################################################################################################################################
#q2b



#mystack = LLStack()
#Without a subclass - not most efficient implementation
class ModStack:
    def __init__(self):
        self._stack = LLStack()
        self._min_stack = LLStack()

    def __len__(self):
        return len(self._stack)
    
    def is_empty(self):
        return self._stack.is_empty()
    
    def push(self, e):  #This needs to be modified to keep track of the smallest 
        self._stack.push(e)
        if self._min_stack.is_empty() or e <= self._min_stack.top():
            self._min_stack.push(e)
            
    def top(self):
        return self._stack.top()
    
    def pop(self):
        popped_element = self._stack.pop()
        if popped_element == self._min_stack.top():
            self._min_stack.pop()

    def smallest(self):
        return self._min_stack.top()
"""
mystack = ModStack()
mystack.push(4)
mystack.push(5)
mystack.push(1)
mystack.push(9)
print(mystack.smallest())
""" 

########################################################################################################################################
#q2c - needs to be with LLQueue to work

def reverse(q):
    #We have a queue - one of the standard ways of reversing a queue is to use a stack.
    stack = []
    while q.is_empty() == False:
        stack.append(q.dequeue())
    q_2 = LLQueue()
    while stack:
        q_2.enqueue(stack.pop())
    return q_2

queue = LLQueue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(7)
print(queue.front())

reversedqueue = reverse(queue)
print(reversedqueue.front())