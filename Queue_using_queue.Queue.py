# Queue implementation using queue module

from queue import Queue
# Initializing a queue
q = Queue(maxsize = 3)

print(q.qsize)

# Adding elements to queue using put() function of queue module
q.put('a')
q.put('b')
q.put('c')

# use full() for returning the boolean value for Full
print('\nFull: ', q.full())

# Removing the element from queue using get()
print('\nElements dequeued from the queue')
print(q.get())
print(q.get())
print(q.get())

# Return boolean value for Empty using empty()
print('\n Empty: ', q.empty())

