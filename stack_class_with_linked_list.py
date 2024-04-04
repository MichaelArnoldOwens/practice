'''
❓ PROMPT
Implement a basic stack class using an linked list as the underlying storage. Stacks have two critical methods,
push() and pop() to add and remove an item from the stack, respectively. You'll also need a constructor for your class,
and for convenience, add a size() method that returns the current size of the stack. All of these methods should run in O(1) time!


Remember, a stack is a last in, first out data structure!

A singly linked list is a simple way to create a stack. The head of the list is the top of the stack.

Example(s)
const stack = new LLStack();
console.log(stack.size()) // 0
stack.push(2);
stack.push(3);
console.log(stack.size()) // 2
console.log(stack.pop()); // 3
console.log(stack.size()) // 1
console.log(stack.pop()); // 2
'''

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def size(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.head is None or self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return None
        self.size -= 1
        temp = self.tail.prev
        self.tail.prev = None
        temp.next = None
        result = self.tail
        self.tail = temp
        return result



