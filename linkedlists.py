class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    

    def delete_node(self, key):
        
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        temp = None
    
    def search(self, key):

        current = self.head
        while current:
            if current.data == key:
                return True

            current = current.next
        
        return False
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data + '\n')
            current = current.next
        
        print("None")
        


# 1. Reverse Linked List
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    head = prev
    return head


# Example Usage:
ll = SinglyLinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.print_list()


''' 
Reverse a Linked List: Iteratively or recursively reversing the nodes of a linked list.
Cycle Detection: Using Floyd's cycle-finding algorithm to detect a cycle in a linked list.
Merge Two Sorted Lists: Merging two sorted linked lists into one sorted linked list.
Intersection of Two Lists: Finding the node at which two singly linked lists intersect.
Nth Node from End: Finding the nth node from the end of a linked list
Middle of the Linked List: Finding the middle node of a linked list using the slow and fast pointer technique
'''