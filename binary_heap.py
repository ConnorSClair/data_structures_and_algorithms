from sys import stderr
import random


class Binary_Heap:
    def __init__(self):
        """ initalise new empty binary heap
        """
        ARBITRARY_VALUE = 0
        self.heap = [ARBITRARY_VALUE]

    def insert(self, value: int) -> None:
        """ Insert value (expecting int) into heap
        """
        self.heap.append(value)
        loc = len(self.heap) - 1
        while True:
            if loc == 1:
                # root node
                break
            parent = self.heap[loc // 2]
            if value < parent:
                # perform swap
                self.heap[loc // 2] = value
                self.heap[loc] = parent
                loc = loc // 2
            else:
                break

    def delete_min(self) -> int:
        """ delete and return smallest value in heap
            error message is displayed and -1 returned if call delete_min when heap is empty
        """
        if len(self.heap) <= 1:
            print(f"No values stored in heap", file=stderr)
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        loc = 1
        while loc * 2 + 1 < len(self.heap):
            # two children
            smallest_loc = loc * 2
            smallest = self.heap[smallest_loc]
            if self.heap[loc * 2 + 1] < smallest:
                # variables reflect right child smaller
                smallest_loc += 1
                smallest = self.heap[smallest_loc]
            if self.heap[loc] > smallest:
                # swap this value with the smallest one
                self.heap[smallest_loc] = self.heap[loc]
                self.heap[loc] = smallest
            loc = smallest_loc
        if loc * 2 < len(self.heap):
            smallest = self.heap[loc * 2]
            if self.heap[loc] > smallest:
                # swap this value with the smallest one
                self.heap[loc * 2] = self.heap[loc]
                self.heap[loc] = smallest
        return result

    def invariant(self) -> bool:
        """ Checks invariant that no child exists such that its key is larger than its parent's key  
        """
        loc = 0
        left_loc = 2 * loc
        right_loc = 2 * loc + 1
        rightmost_leaf_loc = len(self.heap) - 1
        while right_loc <= rightmost_leaf_loc:
            # two children
            this = self.heap[loc]
            left = self.heap[left_loc]
            right = self.heap[right_loc]
            if this > left or this > right:
                print(
                    f"value: {this} at {loc} is larger than a children {left},{right}", file=stderr)
                return False
            else:
                loc += 1
                left_loc = 2 * loc
                right_loc = 2 * loc + 1
        if left_loc == rightmost_leaf_loc:
            # complete, so only enter here if at rightmost_leaf_loc
            return self.heap[loc] <= self.heap[loc * 2]
        return True
