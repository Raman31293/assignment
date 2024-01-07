class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def partition_linked_list(head, partition_value):
    # create two dummy nodes
    dummy1 = Node()
    dummy2 = Node()
    
    # two pointers to iterate through 2 lists
    ptr1, ptr2 = dummy1, dummy2
    
    # traverse through original list and partition through value
    current = head
    while current:
        if current.data < partition_value:
            # then value of current pointer changes
            dummy1.next = current
            # pointer moves to next step
            dummy1 = dummy1.next
        else:
            dummy2.next = current
            dummy2 = dummy2.next
        current = current.next

    # combining two lists and end pointer set to null
    dummy1.next = dummy2.next
    dummy2.next = None
    
    # return head of the new list
    return dummy1.next

# printing linked list
def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next

# Creating a linked list: 1 -> 10 -> 5 -> 15 -> 50
linked_list = Node(1)
linked_list.next = Node(10)
linked_list.next.next = Node(5)
linked_list.next.next.next = Node(15)
linked_list.next.next.next.next = Node(50)

# Partitioning the linked list with partition_value = 5
partitioned_list = partition_linked_list(linked_list, 15)

# Printing the original and partitioned lists
print("Original Linked List:")
print_list(linked_list)

print("\nPartitioned Linked List:")
print_list(partitioned_list)