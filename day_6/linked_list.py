# linked list is a collection of nodes
# Components of a Linked List

# A Linked List is made up of nodes.

# Each node has 2 main components:

# Data → stores the value
# Next Pointer (next) → stores the address of the next node

# data type of address node is node

# | Component  | Purpose                       |
# | ---------- | ----------------------------- |
# | Head       | Points to the first node      |
# | Data (val) | Stores the value              |
# | Next       | Points to the next node       |
# | Tail       | Last node of the list         |
# | None       | Indicates the end of the list |

# creating a node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create nodes
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

# Connect nodes
node1.next = node2
node2.next = node3

# Print linked list
current = node1

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")