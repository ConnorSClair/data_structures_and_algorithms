from binary_heap_implementation import *
from sort import *
from hash_table import *
from dfs import *
from tree_traversal import *

def binary_heap_tests():
    heap = Binary_Heap()
    for i in range(30):
        value = random.randrange(1,1000)
        heap.insert(value)
    for i in range(20):
        print(heap.delete_min())
    for i in range(30):
        value = random.randrange(1,1000)
        heap.insert(value)
    for i in range(40):
        print(heap.delete_min())
    heap.delete_min()

def sorted_tests():
    arr = []
    for i in range(50):
        arr.append(random.randrange(1,100))
    test = arr.copy()
    test.sort()
    arr = pivot_sort(arr)
    if test == arr:
        print("passed sorted")
    else:
        print(f"failed sorted expected: {test} output: {arr}")

def hash_table_tests():
    table = Hash_Table()
    for i in range(50):
        table.add(random.randrange(1,100))
    print(table.table)

def is_cyclic_graph_test():
    simple_graph_cyclic= {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['E'],
    'E': ['B', 'F'],
    'F': ['C']
    }
    simple_graph_not_cyclic = {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['E'],
    'E': ['F'],
    'F': ['C']
    }
    print(f"Expected TRUE, found {is_cycle(simple_graph_cyclic)}")
    print(f"Expected FALSE, found {is_cycle(simple_graph_not_cyclic)}")

def test_traversal():
    simple_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
    }
    traverse("A",simple_tree,Traversal_Type.IN_ORDER)
    traverse("A",simple_tree,Traversal_Type.POST_ORDER)
    traverse("A",simple_tree,Traversal_Type.PRE_ORDER)



if __name__ == "__main__":
    #binary_heap_tests()
    #sorted_tests()
    #hash_table_tests()
    #is_cyclic_graph_test()
    test_traversal()