from collections import deque

print_queue = deque()

print_queue.append("Document A")
print_queue.append("Document B")
print_queue.append("Document C")

print(print_queue)

while print_queue:
    current_job = print_queue.popleft()
    print( "Printing: "  ,current_job)

print("All Done , Queue is now: ", print_queue)    



