#to demonstrate queue implementation using list

queue = []

#append() to push element in queue
queue.append('a')
queue.append('b')
queue.append('c')


print('The initial queue is:-')
print(queue)


# pop(0) to remove the element from queue in FIFO order
print('\nOrder of elements removed from the queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nThe queue after the elements are removed')
print(queue)