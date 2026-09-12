class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_all(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

def insert_after(prev_node, new_data):
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

def delete_after(prev_node):
    if prev_node.next is not None:
        prev_node.next = prev_node.next.next

def update_node(head, target_data, new_data):
    current = head
    while current is not None:
        if current.data == target_data:
            current.data = new_data
            return
        current = current.next

# ---- Setup ----
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
head = node1

print("Original list:")
print_all(head)                       # 10 20 30

# ---- Insertion task ----
insert_after(node1, 15)               # insert 15 after node1 (10)
print("After inserting 15:")
print_all(head)                        # 10 15 20 30

# ---- Deletion task ----
delete_after(node1)                    # delete whatever comes right after node1
print("After deleting the node after 10:")
print_all(head)                         # 10 20 30

# ---- Update task ----
update_node(head, 20, 99)              # find node with data=20, change it to 99
print("After updating 20 to 99:")
print_all(head)                          # 10 99 30