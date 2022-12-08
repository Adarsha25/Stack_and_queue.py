# Queue implememtation using collections.dequeue
from collections import deque
q = deque()

# Adding elements to queue
q.append('a')
q.append('b')
q.append('c')

print('Initial queue:-')
print(q)

#Removing the elements from the queue
print('\nElements dequeued from the queue')
print(q.popleft())
print(q.popleft())
print(q.popleft())

print('\nQueue after removing the elements')
print(q)