class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList

    while currentNode.next is not None:
        temp = currentNode.next
        if temp.value == currentNode.value:
            currentNode.next = temp.next
        else:
            currentNode = currentNode.next

    return linkedList


linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next.next.next = LinkedList(6)
linkedList.next.next.next.next.next.next.next.next = LinkedList(6)

result = removeDuplicatesFromLinkedList(linkedList)

while result is not None:
    print(result.value)
    result = result.next


