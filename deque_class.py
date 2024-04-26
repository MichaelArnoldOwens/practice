'''
❓ PROMPT
A deque is a limited access data structure that combines features of stacks and queues. A deque efficiently supports operations on both ends, both adds and removes, but does not support modifications in the middle. If you're a Python programmer, you've probably seen the built in deque class and it's often a handy way to get queue behavior efficiently, without the cost of a linear time shift operation.

As a practice exercise, we're going to build a deque class from scratch. The key decision is what you will use for the internal data structure to manage elements. As a thought exercise ahead of writing any code you might want to consider:

- How might you implement a deque if you know when the object is constructed what the maximum capacity needs to be?
- What is a good implementation choice if you don't have any idea what the capacity needs to be?

There are multiple ways to build a deque that all satisfy the requirements for the operations to be constant time! As in any engineering situation, there are tradeoffs!

We recommend building at least two entirely different designs for this one. The two we have in mind are both great exercises and will help build skill in different areas!

Example(s)
d = new Deque()

d.push(1)
d.push(2)
d.peek() -> returns 2
d.peekleft() -> returns 1
d.pushleft(0)
d.size() -> returns 3
d.peekleft() -> returns 0
d.pop() -> returns 2
d.popleft() -> returns 0
d.size() -> returns 1
'''
class LLNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Deque1:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def push(self, value):
        if not self.head:
            self.head = LLNode(value)
            self.tail = self.head
            self.size += 1
        else:
            new_node = LLNode(value, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def pushleft(self, value):
        if not self.head:
            self.push(value)
        else:
            new_node = LLNode(value, next=self.head)
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.tail:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.size -= 1
            return temp.value

    def popleft(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
            self.size -= 1
            return temp.value

    def peek(self):
        if self.tail:
            return self.tail.value

    def peekleft(self):
        if self.head:
            return self.head.value




d = Deque1()
d.push(1)
d.push(2)
print(d.peek())
print(d.peekleft())
d.pushleft(0)
print(d.size)
print(d.peekleft())
print(d.pop())
print(d.popleft())
print(d.size)
