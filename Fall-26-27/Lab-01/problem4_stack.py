# Problem 4 - Stack (LIFO) using a list
# The last element added is the first one taken out.
# append() pushes onto the top, pop() removes from the top.

stack = []

# push
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack after pushing A, B, C:", stack)

# peek (look at the top without removing it)
print("Top element:", stack[-1])

# pop
top = stack.pop()
print("Popped:", top)
print("Stack now:", stack)

stack.append("D")
print("Pushed D:", stack)

# pop everything until the stack is empty
while len(stack) > 0:
    print("Popped:", stack.pop())

print("Is the stack empty?", len(stack) == 0)
