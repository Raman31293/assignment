# Creating a Node class for the linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Function to merge two linked lists in-place
def merge_in_place(list1, list2):
    dummy = Node()
    current = dummy
    ptr1, ptr2 = list1, list2

    while ptr1 and ptr2:
        if ptr1.data < ptr2.data:
            current.next = ptr1
            ptr1 = ptr1.next
        else:
            current.next = ptr2
            ptr2 = ptr2.next
        current = current.next

    if ptr1:
        current.next = ptr1
    elif ptr2:
        current.next = ptr2

    return dummy.next

# Function to print the merged linked list
def merged_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next

# Creating instances of the Node class for two linked lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(7)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(5)
list2.next.next.next = Node(6)

# Merging the linked lists and printing the result
merged_list = merge_in_place(list1, list2)
merged_linked_list(merged_list)
