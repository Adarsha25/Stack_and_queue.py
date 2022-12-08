# Stacke implementation using queue module
from queue import LifoQueue
stack = LifoQueue(maxsize=3)

print(stack.qsize())

# put() fuction to push elements in the stack
stack.put ('a')
stack.put ('b')
stack.put ('c')

# stack.full() returns the boolean value 'True' if stack is full or 'False'
# stack.qsize() returns the size of the stack
print('Full: ', stack.full())
print(stack.get())
print(stack.get())
print(stack.get())

print('\nEmpty: ', stack.empty())

