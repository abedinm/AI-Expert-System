# Problem 5 - Queue (FIFO) using a list
# The first element added is the first one taken out.
# append() adds to the back, pop(0) removes from the front.

queue = []

# enqueue
queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")
print("Queue:", queue)

# look at the front without removing it
print("Front of queue:", queue[0])

# dequeue
first = queue.pop(0)
print("Served:", first)
print("Queue now:", queue)

queue.append("Customer 4")
print("Customer 4 joined:", queue)

# serve everyone in order
while len(queue) > 0:
    print("Served:", queue.pop(0))

print("Is the queue empty?", len(queue) == 0)
