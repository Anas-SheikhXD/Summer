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

def insert_after(previous_node , new_data):
    new_node = Node(new_data)
    new_node.next = previous_node.next
    previous_node.next = new_node

def after_deletion(previous_node):
    if previous_node is not None:
        previous_node.next = previous_node.next.next

def update_node(head, target_data, new_data):
    current = head
    while current is not None:
        if current.data == target_data:
            current.data = new_data
            return
        current = current.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

print("Orignal List: ") 
print_all(head)

insert_after(node1, 15)
print("List after Inserting 15: ")
print_all(head)

after_deletion(node1)
print("List after Deletion of 15: ")
print_all(head)

update_node(head, 20 , 99)
print("Printing after Updating: ")
print_all(head)