import unittest

import singly_linked_list as linkedList


class Test(unittest.TestCase):
    def setUp(self):
        print "In method", self._testMethodName

    def test_Created_LinkedList_NodesNumber(self):
        llist = linkedList.SinglyLinkedList()
        self.assertEqual(llist.numberOfNodes(),0)

        llist.insertNode(32)
        llist.insertNode(132)
        llist.insertNode(4)
        self.assertEqual(llist.numberOfNodes(), 3)

        llist.deleteNodeAtIndex(0)
        self.assertEqual(llist.numberOfNodes(), 2)

        llist.deleteAllNodes()
        self.assertEqual(llist.numberOfNodes(), 0)

    def test_Create_Add_Delete_Nodes(self):
        llist = linkedList.SinglyLinkedList()

        llist.insertNodeAtIndex(0,1)
        self.assertEqual(llist.getAllNodes(), [1])

        llist.deleteAllNodes()

        llist.insertNode(32)
        llist.insertNode(132)
        llist.insertNode(4)
        self.assertEqual(llist.getAllNodes(), [32,132,4])

        llist.insertNodeAtIndex(1,11)
        self.assertEqual(llist.getAllNodes(), [32,11,132,4])

        llist.insertNodeAtIndex(10,99)
        self.assertEqual(llist.getAllNodes(), [32,11,132,4])

        llist.insertNodeAtIndex(2,10101)
        self.assertEqual(llist.getAllNodes(), [32,11,10101,132,4])

        llist.insertNodeAtIndex(0,9009)
        self.assertEqual(llist.getAllNodes(), [9009,32,11,10101,132,4])

    def test_GetNode_From_Particular_Index(self):
        llist = linkedList.SinglyLinkedList()

        llist.insertNode(32)
        llist.insertNode(132)
        llist.insertNode(4)
        self.assertEqual(llist.getNodeAtIndex(0).element, 32)

        self.assertEqual(llist.getNodeAtIndex(1).element, 132)

        self.assertEqual(llist.getNodeAtIndex(2).element, 4)
        self.assertEqual(llist.getNodeAtIndex(2).next, None)

        self.assertEqual(llist.getNodeAtIndex(4).element, None)
        self.assertEqual(llist.getNodeAtIndex(4).next, None)

    def test_DeleteNode_From_Particular_Index(self):
        llist = linkedList.SinglyLinkedList()

        llist.insertNode(32)
        llist.insertNode(132)
        llist.insertNode(4)
        llist.insertNode(24)
        llist.insertNode(1114)
        llist.deleteNodeAtIndex(1)

        self.assertEqual(llist.getAllNodes(), [32,4,24,1114])

        llist.deleteNodeAtIndex(0)
        self.assertEqual(llist.getAllNodes(), [4,24,1114])

        llist.deleteNodeAtIndex(2)
        self.assertEqual(llist.getAllNodes(), [4,24])



if __name__ == '__main__':
    unittest.main()