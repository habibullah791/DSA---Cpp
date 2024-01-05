# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseKchunks(linkedList, k):
    if linkedList is None:
        return None

    currentNode = linkedList
    prevNode = None
    nextNode = None

    count = 0

    # c n
    # 1 2 3 4 5 6 7
    while currentNode is not None and count < k:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
        count += 1

    if nextNode is not None:
        linkedList.next = reverseKchunks(nextNode, k)

    return prevNode

linkedList = LinkedList(1)
linkedList.next = LinkedList(2)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next = LinkedList(6)
linkedList.next.next.next.next.next.next = LinkedList(7)

result = reverseKchunks(linkedList, 3)

while result is not None:
    print(result.value, end=" ")
    result = result.next