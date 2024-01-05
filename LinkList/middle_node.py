# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slowPtr = linkedList
    fastPtr = linkedList

    while fastPtr and fastPtr.next:
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

    return slowPtr


linkedList = LinkedList(2)
linkedList.next = LinkedList(7)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(5)

result = middleNode(linkedList)
print(result)
