#!/usr/bin/python3
"""A FILE THAT DEFINES CLASSES FOR A singly-linked list."""


class Node:
    """A CLASS THAT REPRESENTS A NODE."""

    def __init__(self, data, next_node=None):
        """USED TO Initialize A NEW NODE.

        Args:
            data (int): REPRESENTS THE DATA/INFO OF NEW NODE.
            next_node (Node): REPRESENTS THE NEXT NODE OF NEW NODE..
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """A FUNCTION THAT FETCHES DATA/INFO OF NODE.."""

        return (self.__data)

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """A FUNCTION THAT FETCHES THE NEXT NODE OF THE NODE.."""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A CLASS THAT REPRESENTS A singly-linked list."""

    def __init__(self):
        """USED TO Initialize A NEW SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """A FUNCTION THAT INSERTS A NEW NODE TO SinglyLinkedList.

        IT'S INSERTED AT THE CORRECT ORDER.

        Args:
            value (Node): REPRESENTS THE NEW NODE TO BE INSERTED.
        """

        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """A FUNCTION THAT DEFINES the print()
        REPRESENTATION OF A SinglyLinkedList."""

        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
