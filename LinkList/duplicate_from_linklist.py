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
def test(linkedList):
    x = linkedList
    while x is not None:                      
        y = x.next
        while y is not None and (y.value % x.value == 0):
            y_old = y
            y = y.next
            y_old = None
        x.next = y
        x = x.next

    return linkedList
        
linkedList = LinkedList(4)
linkedList.next = LinkedList(8)
linkedList.next.next = LinkedList(12)
linkedList.next.next.next = LinkedList(5)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(2)
linkedList.next.next.next.next.next.next = LinkedList(3)
linkedList.next.next.next.next.next.next.next = LinkedList(5)



result = test(linkedList)
# result = removeDuplicatesFromLinkedList(linkedList)

while result is not None:
    # print(111)
    print(result.value)
    result = result.next


