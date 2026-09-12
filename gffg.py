class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Connect them
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Keep track of the head — the starting point
head = node1

def get_third_node(head):
    current = head
    current = current.next
    current = current.next
    return current.data

print(get_third_node(head))

def print_all(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


print_all(head)


