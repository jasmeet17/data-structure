class SinglyLinkedList(object):
    """docstring for SinglyLinkedList"""
    def __init__(self, name="Test"):
        super(SinglyLinkedList, self).__init__()
        self.name = name
        self.head = None
        self.tail = None

    def insertNode(self, value):
        if self.head is None:
            self.head = self.tail = Node(value, None)
        else:
            node = self.getLastNode()
            node.next = Node(value, None)

    def insertNodeAtIndex(self, index, value):
        if index == 0 and self.head == None:
            self.insertNode(value)
        elif index == 0:
            newNode = Node(value, self.head)
            self.head = newNode
        else:
            node = self.getNodeAtIndex(index-1)

            if node.element == None:
                return
            else:
                newNode = Node(value, node.next)
                node.next = newNode

    def getNodeAtIndex(self, index):
        node = self.head
        currentIndex = 0

        while hasattr(node, 'element') and currentIndex != index:
            currentIndex += 1

            if node.next != None:
                node = node.next
            else:
                node = Node(None, None)

        if hasattr(node, 'element'):
            return node
        else:
            return Node(None, None)

    def getLastNode(self):
        node = self.head

        while hasattr(node, 'element'):
            if node.next != None :
                node = node.next
            else:
                return node

        if node == None:
            node = Node(None, None)

        return node


    def deleteAllNodes(self):
        self.head = None

    def deleteNodeAtIndex(self, index):
        if index == 0:
            self.head = self.head.next if hasattr(self.head, 'next') else None
        else:
            nodeBefore = self.getNodeAtIndex(index-1)
            if nodeBefore.element == None or nodeBefore.next == None:
                return
            else:
                nodeToDelete = nodeBefore.next
                if nodeToDelete.next == None:
                    nodeBefore.next = None
                else:
                    nodeBefore.next=nodeToDelete.next


    def getAllNodes(self):
        nodes = []
        node = self.head

        while hasattr(node, 'element'):
            nodes.append(node.element)
            node = node.next

        return nodes

    def getFirstNode(self):
        node = self.head

        if node == None:
            node = Node(None, None)

    def numberOfNodes(self):
        node = self.head
        numberOfNodes = 0

        while hasattr(node, 'element'):
            node = node.next
            numberOfNodes += 1

        return numberOfNodes

    def printAllValues(self):
        node = self.head

        while hasattr(node, 'element'):
            print node.element
            node = node.next

class Node(object):
    """docstring for Node"""
    def __init__(self, value, nextNode):
        super(Node, self).__init__()
        self.element = value
        self.next = nextNode

if __name__ == '__main__':
    unittest.main()
