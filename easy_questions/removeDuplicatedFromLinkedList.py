# This is an input class. Do not edit.
class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # set initial nodes
    c_node = linkedList

    # Remove till find last node in linkedList
    while c_node:
        n_node = c_node.next
        # return if current node is the last node
        if not n_node:
            break
    # if currnet value equal with next value
        if c_node.value == n_node.value:
            # drop the next node, set c_node.next with n_node.next
            n_node = n_node.next
            c_node.next = n_node
        else:
            # if values are different, move to next node
            c_node = n_node
            n_node = n_node.next

    return linkedList
