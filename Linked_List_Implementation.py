# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next as None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head of the linked list as None

    # Function to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty
            self.head = new_node  # Make the new node the head
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Add the new node at the end

    # Function to insert a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the new head

    # Function to insert a new node after a specific node
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("The previous node is not in the list.")
            return
        new_node = Node(data)  # Create the new node
        new_node.next = prev_node.next  # Link the new node to the next of the previous node
        prev_node.next = new_node  # Link the previous node to the new node

    # Function to delete a node with a specific value
    def delete_node(self, key):
        temp = self.head

        # If the head node itself holds the key to be deleted
        if temp and temp.data == key:
            self.head = temp.next  # Change the head to the next node
            temp = None  # Free memory
            return

        # Search for the key to be deleted, keeping track of the previous node
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If the key is not present in the list
        if temp is None:
            print("Key not found in the list.")
            return

        prev.next = temp.next  # Unlink the node from the linked list
        temp = None  # Free memory

    # Function to display the contents of the list
    def display(self):
        temp = self.head
        if temp is None:
            print("The list is empty.")
            return
        print("Linked List: ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)

ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

ll.insert_after(ll.head.next, 15)  # Insert 15 after 10
ll.display()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> None

ll.delete_node(20)
ll.display()  # Output: 5 -> 10 -> 15 -> 30 -> None
