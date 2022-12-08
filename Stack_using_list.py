#to demonstrate stack implementation using list

stack = []

#append() to push element in stack
stack.append('a')
stack.append('b')
stack.append('c')


print('The initial stack is:-')
print(stack)


# pop() to remove the element from stack in LIFO order
print('\nOrder of elements removed from the stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nThe stack after the elements are removed')
print(stack)