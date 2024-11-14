#3ASSIGNMENT4ARC
class Node:
    def __init__(self, value=None, next=None, previous=None):
        # Define the node's basic properties "value", "next", "previous" and default them
        self.value = value
        self.next = next
        self.previous = previous

    def set(self, value):
        # Set this node's value to the given value
        self.value = value
        return self

    def get_value(self):
        # Return the value of this node
        return self.value

    def get_next(self):
        # Return this node's next node
        return self.next

    def get_previous(self):
        # Return this node's previous node
        return self.previous

    def set_next(self, next):
        # Set this node's next node
        self.next = next
        return self

    def set_previous(self, previous):
        # Set this node's previous node
        self.previous = previous
        return self

# the class for the Linked list
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
#checking is if empty
    def is_empty(self):
        return self.size == 0

#function to add
    def add(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.set_next(new_node)
            new_node.set_previous(self.last)
            self.last = new_node
        self.size += 1

#function to remove
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.first = self.first.get_next()
            if self.first:
                self.first.set_previous(None)
        else:
            current_node = self.first
            for _ in range(index - 1):
                current_node = current_node.get_next()

            current_node.set_next(current_node.get_next().get_next())
            if current_node.get_next():
                current_node.get_next().set_previous(current_node)

        self.size -= 1

#function to get
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current_node = self.first
        for _ in range(index):
            current_node = current_node.get_next()
        return current_node.get_value()

#function to get the first
    def get_first(self):
        if self.is_empty():
            return None
        return self.first.get_value()

#function to get the last
    def get_last(self):
        if self.is_empty():
            return None
        return self.last.get_value()

#function to reverse it
    def reverse(self):
        if self.is_empty():
            return
        current_node = self.first
        while current_node:
            current_node.previous, current_node.next = current_node.next, current_node.previous
            current_node = current_node.previous

        self.first, self.last = self.last, self.first

#function for the output
    def print_list(self):
        current_node = self.first
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next 

        print()


my_list = LinkedList()
my_list.add(10)
my_list.add(20)
my_list.add(30)

print("Original list:")
my_list.print_list()

print("Reversed list:")
my_list.reverse()
my_list.print_list()