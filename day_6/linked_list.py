# # linked list is a collection of nodes
# # Components of a Linked List

# # A Linked List is made up of nodes.

# # Each node has 2 main components:

# # Data → stores the value
# # Next Pointer (next) → stores the address of the next node

# # data type of address node is node

# # | Component  | Purpose                       |
# # | ---------- | ----------------------------- |
# # | Head       | Points to the first node      |
# # | Data (val) | Stores the value              |
# # | Next       | Points to the next node       |
# # | Tail       | Last node of the list         |
# # | None       | Indicates the end of the list |

# # creating a node
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



### Types of Linked Lists(4)


# # 1. Singly Linked List (SLL)

# Each node points to the next node.
# 10 → 20 → 30 → None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# ✅ Less memory
# ❌ Cannot move backward

# # 2. Doubly Linked List (DLL)

# Each node has two pointers:
# * `prev`
# * `next`

# None ← 10 ⇄ 20 ⇄ 30 → None

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


# ✅ Traverse forward and backward
# ❌ Extra memory for `prev`

# # 3. Circular Singly Linked List (CSLL)

# Last node points back to the first node.

# 10 → 20 → 30
# ↑         ↓
# └─────────┘

# 30.next = 10


# ✅ No `None` at the end
# ✅ Useful in round-robin scheduling


# ## 4. Circular Doubly Linked List (CDLL)

# Both forward and backward circular links.


#       ⇄ 10 ⇄ 20 ⇄ 30 ⇄
#       ↑               ↓
#       └───────────────┘


# * Last node's `next` → Head
# * Head's `prev` → Last node

# ✅ Traverse in both directions endlessly
# ❌ Most memory usage

# ### Quick Comparison

# | Type               | Next Pointer | Prev Pointer | Circular |
# | ------------------ | ------------ | ------------ | -------- |
# | Singly LL          | ✅            | ❌            | ❌        |
# | Doubly LL          | ✅            | ✅            | ❌        |
# | Circular Singly LL | ✅            | ❌            | ✅        |
# | Circular Doubly LL | ✅            | ✅            | ✅        |