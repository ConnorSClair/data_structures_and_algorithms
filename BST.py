import typing
import collections
class Node:
    def __init__(self,parent,left,right,key):
        # references to nodes
        self.left = left
        self.right = right
        self.parent = parent 
        # key
        self.key = key
        # subtree heights 
        self.left_height = 0
        self.right_height = 0

    def get_heights(self):
        if self.left != None:
            self.left_height = max(self.left.left_height, self.left.right_height)
        if self.right != None:
            self.right_height = max(self.right.left_height, self.right.right_height)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        # root node 
        if self.root == None:
            self.root = Node(None,None,None,key)
        else:
            node = self.root
            while True:
                if key > node.key:
                    #right
                    if node.right == None:
                        node.right = Node(node,None,None,key)
                        break
                    else:
                        node = node.right
                else:
                    #left
                    if node.left == None:
                        node.left = Node(node,None,None,key)
                        break
                    else:
                        node = node.left
        
    
    def search(self,key):
        """ Returns True if found, otherwise False"""
        return self.__find(key) != None
    
    def __find(self,key):
        """ Returns Node if found, otherwise None """
        node = self.root
        while node != None:
            if key == node.key:
                return node
            elif key > node.key:
                # right
                node = node.right
            else:
                node = node.left
        return None
    
    def successor(self,key):
        # find smallest key in tree larger than key
        # search to the leaf node as if trying to find it. then return node 
        key = key + 1
        node = self.root
        while node != None:
            if key == node.key:
                return node
            elif key > node.key:
                # right
                node = node.right
            else:
                node = node.left
        return node


    def remove(self,key):
        """ Returns true if removed, or false if not found"""
        node = self.__find(key)
        if node == None:
            return False
        parent = node.parent
        if parent == None:
            # root node 
            if node.left == None and node.right == None:
                self.root = None
            elif node.left == None != node.right == None:
                if node.left != None:
                    self.root = node.left
                else:
                    self.root = node.right
            else:
                successor = self.successor(key)
                self.root = successor
                self.remove(successor)
        # simplest case - no children
        if node.left == None and node.right == None:
            # fix parent references
            if parent.left == node:
                parent.left = None
            if parent.right == node:
                parent.right = None
        elif node.left == None != node.right == None:
            # one child
            if node.left != None:
                new_child = node.left
            else:
                new_child = node.right
            if parent.left == node:
                parent.left = new_child
            else:
                parent.right = new_child
        else:
            # two children. find succ...
            successor = self.successor(key)
            if parent.left == node:
                parent.left = successor
            else:
                parent.right = successor
            successor_parent = successor.parent
            if successor_parent.left == successor:
                successor_parent.left = node
            else:
                successor_parent.right = node
            # swap the values 
            self.remove(node.key)


    def __invariant(self,node: Node):
        # assume unique keys
        result = True
        if node == None:
            return True
        if node.left != None:
            result = node.key > node.left.key
        if node.right != None:
            result = result and (node.key < node.right.key)
        return result
        

    def check_invariant(self,node):
        # this.key < all children of left.key and this.key > all children of right.key
        # Preorder traversal 
        if node == None:
            return True
        else:
            return self.__invariant(node) and self.check_invariant(node.left) and self.check_invariant(node.right)
    
    def __repr__(self):
        result = ""
        if self.root == None:
            return result
        q = collections.deque()
        levels = collections.deque()
        q.append(self.root)
        levels.append(0)
        level = 0
        # because tree, don't worry about cycles
        while len(q) > 0:
            if levels[0] == -1:
                levels.popleft()
                result += "_"
            if level < levels[0]:
                result += "\n"
            this = q.popleft()
            level = levels.popleft()
            result += str(this.key)

            if this.left != None:
                q.append(this.left)
                levels.append(level + 1)
            else:
                levels.append(-1)
            if this.right != None:
                q.append(this.right)
                levels.append(level + 1)
            else:
                levels.append(-1)
            
        return result

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(5)
    bst.insert(7)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    print(bst)
    # remove leaf node
    bst.remove(7)
    print(bst)
    # remove node with one subtree
    bst.insert(7)
    bst.remove(5)
    print(bst)
    bst.remove(2)
    print(bst)
    bst.insert(2)
    bst.insert(5)
    #bst.remove(4)
    #print(bst)