#!/usr/bin/env python
# coding: utf-8

# In[9]:


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
            raise Exception
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        return answer

#mystack = LLStack()


class LLQueue:
    """
    Implements a queue using a singly-linked list.

    Example usage:

      myqueue = LLQueue()
      myqueue.enqueue(3)

    You must not modify this implementation or include 
    it in your submission.
    """

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise Exception

        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

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


