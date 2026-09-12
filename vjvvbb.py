from collections import deque

queue = deque()

#enqued items
queue.append("A1")
queue.append("BYEBYE WORLD")
queue.append("Hello World")

print(queue)

deque_item = queue.popleft() # dequed item
print(deque_item)

print(queue)

