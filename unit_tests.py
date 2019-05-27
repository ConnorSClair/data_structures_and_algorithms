import unittest
from BST import *
import random

class TestBinarySearchTree(unittest.TestCase):


    def test_insertion(self):
        bst = BinarySearchTree()
        bst.insert(4)
        bst.insert(5)
        bst.insert(7)
        bst.insert(2)
        bst.insert(3)
        bst.insert(1)
        self.assertEquals(str(bst),"4\n25\n13_7")
        self.assertTrue(bst.check_invariant(bst.root))
        bst.root.right.key = 0
        self.assertFalse(bst.check_invariant(bst.root))
        bst.root.right.key = 5
    
    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(4)
        # single elem - TRUE
        self.assertTrue(bst.search(4))
        # single elem - FALSE
        self.assertFalse(bst.search(3))
        self.assertFalse(bst.search(5))

        bst.insert(2)
        bst.insert(5)
        # Multi elem - FALSE
        self.assertFalse(bst.search(6))
        self.assertFalse(bst.search(3))
        self.assertFalse(bst.search(1))
        # Multi elem - TRUE
        self.assertTrue(bst.search(4))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(5))
        
        bst.insert(10)
        bst.insert(1)
        bst.insert(-5)
        # Complicated - TRUE 
        self.assertTrue(bst.search(-5))
        # Complicated - FALSE
        self.assertFalse(bst.search(-10))
        self.assertTrue(bst.check_invariant(bst.root))

if __name__ == "__main__":
    unittest.main()
        

    
