# Stack implementation using collections.deque
from collections import deque

stack = deque()

# append() to push element in stack
stack.append('a')
stack.append('b')
stack.append('c')

print('The initial stack is:-')
print(stack)

print('\nOrder in which elements are removed are')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after the elements are removed')
print(stack)