from binary_heap_implementation import *
if __name__ == "__main__":
    heap = Binary_Heap()
    for i in range(30):
        value = random.randrange(1,1000)
        heap.insert(value)
    for i in range(20):
        print(heap.delete_min())
    print(heap.invariant()) 
    for i in range(30):
        value = random.randrange(1,1000)
        heap.insert(value)
    for i in range(40):
        print(heap.delete_min())
    print(heap.invariant()) 
    heap.delete_min()