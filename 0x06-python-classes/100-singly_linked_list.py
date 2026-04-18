#!/usr/bin/python3
""" Module that defines a Node class. """


class Node:
    """ Define a node of a singly likend list. """
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.data = data

        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.next_node = next_node

    """ Geter for the private instance attribute data. """
    @property
    def data(self):
        return self.__data

    """ Seter for the private instance attribute data. """
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    """ Geter for the private instance attribute next_node. """
    @property
    def next_node(self):
        return self.__next_node

    """ Seter for the private instance attribute next_node. """
    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" Module that defines a SinglyLinkedList class. """


class SinglyLinkedList:

    """ Initialize a new single linked list. """
    def __init__(self):
        self.__head = None

    """ Makes this class pritable. """
    def __str__(self):
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node

        return "\n".join(result)

    """ Insert a new Node into the correct sorted position in the list. """
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None
                    and current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
