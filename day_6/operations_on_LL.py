# # creating a linked list
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # Create nodes
# node1 = ListNode(10)
# node2 = ListNode(20)
# node3 = ListNode(30)

# # Connect nodes
# node1.next = node2
# node2.next = node3

# # Print values
# print(node1.val)
# print(node2.val)
# print(node3.val)

# # output
# # 10
# # 20
# # 30

# #  by traversing
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# node1 = ListNode(10)
# node2 = ListNode(20)
# node3 = ListNode(30)

# # linking nodes
# node1.next = node2
# node2.next = node3

# current = node1

# while current:
#     print(current.val, end=" -> ")
#     current = current.next

# print("None")

# # output
# # 10 -> 20 -> 30 -> None


# # INSERTION

# New node to insert at beginning
new_node = ListNode(5)

# Insert at beginning
new_node.next = head
head = new_node


# code for insertion at beginning
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Existing Linked List
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)

# New node to insert at beginning
new_node = ListNode(5)

# Insert at beginning
new_node.next = head
head = new_node
return head

# # Print Linked List
# current = head

# while current:
#     print(current.val, end=" -> ")
#     current = current.next

# print("None")


# # insert at end
# new_node = ListNode(40)

# current = head

# while current.next:
#     current = current.next

# current.next = new_node

# # insert at middle

# # code for inserting at middle
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # Create linked list
# head = ListNode(10)
# head.next = ListNode(20)
# head.next.next = ListNode(30)

# # New node
# new_node = ListNode(25)

# # Node after which we want to insert
# current = head.next      # Node with value 20

# # Insert
# new_node.next = current.next
# current.next = new_node

# temp = head

# while temp:
#     print(temp.val, end=" -> ")
#     temp = temp.next

# print("None")



# # deletion





# # traversing

