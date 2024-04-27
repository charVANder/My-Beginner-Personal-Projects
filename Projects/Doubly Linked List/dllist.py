'''
Evangeline Kim
February 23rd, 2024
DS5010: Double-linked list class
'''

class DLList:
    '''Class name: DLList
    Attributes: head (Node), tail (Node)
    Methods: of() (static method), insert(), remove(), __str__(), __iter__(), make_list()
    '''
    class Node:
        '''Class name: Node
        Attributes: value, next (Node), prev (Node)
        Methods: None
        '''
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    @staticmethod
    def of(*nodes):
        '''Static method that creates a new instance of DLList and inserts given nodes. 
        Parameters: All the nodes being inserted into the list (*nodes)
        Returns: The instance containing the nodes.
        '''
        lst = DLList()
        if nodes:
            for node in nodes:
                lst.insert(node)
        else: # Return empty DLList object
            lst.head = None
            lst.tail = None
        return lst
        
    def __init__(self):
        '''This is the Constructor which creates a new instance of DLList
        Parameters: The current object (self)
        Returns: New instance with head and tail set to None.
        '''
        self.head = None
        self.tail = None

    def insert(self, node, location=None):
        '''Inserts a node into the list after the specified location node.
        Parameters: The current object (self), The node to insert (node), the reference locations next/prev the inserted node (location)
        Returns: The updated list.
        '''
        # Setting next/prev references of node being inserted
        node.next = location
        node.prev = location.prev if location else self.tail
        
        # Updating head and tail
        if location == self.head:
            self.head = node
        if location is None:
            self.tail = node
        
        # Updating the other node reference locations
        if node.prev:
            node.prev.next = node
        if node.next:
            node.next.prev = node
        
        return self

    def remove(self, node):
        '''Removes a specified node from the list.
        Parameters: The current object (self), the node to remove (node)
        Returns: The updated list.
        '''
        # Updating next/prev reference locations of the other nodes after removal
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        # Update head/tail if the node is the only one in the list
        if not node.next and not node.prev:
            self.head = None
            self.tail = None
        
        # Clearing the next/prev references of the removed node
        node.next = None
        node.prev = None
        
        return self
    
    def __str__(self):    
        '''Provides the string version of the list and "Empty" if empty.
        Parameters: The current object (self)
        Returns: String version of the list.
        '''
        if self.head is None:
            return "Empty"
        return ' '.join(str(node.value) for node in self)

    def __iter__(self):
        '''Allows iteration over the nodes in the list. This is so that str(l)/list(l) will work correctly.
        Parameters: The current object (self)
        Returns: None, but it yields node values and provides an iterator for the nodes in the list.
        '''
        current_node = self.head
        while current_node: # Iterating until end of list
            yield current_node # Returning the current node's value
            current_node = current_node.next

    def make_list(self):
        '''Converts the list to a Python list of values. This way list(l) will look better.
        Parameters: The current object (self)
        Returns: Python list with all the node values in the linked list.
        '''
        return [node.value for node in self]