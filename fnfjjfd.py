class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect them
node1.next = node2
node2.next = node3

# Keep track of the head — the starting point
head = node1

# Traverse from head to the end
current = head
while current is not None:
    print(current.data)
    current = current.next


      