from random import randrange

# See universal function definition... 

class Hash_Table:
    def __init__(self):
        self.values = 0 
        self.buckets = 11 # initial capacity
        self.table = [[]]*self.buckets
        self.LOAD_FACTOR = 0.75 #see java implementation

    def is_full(self):
        return self.values > self.buckets * self.LOAD_FACTOR

    def hash_(self,val):
        a = randrange(0,self.buckets - 1)
        result = (a * val) % self.buckets
        return result

    def add(self,val):
        h = self.hash_(val)
        self.table[h].append(val)
        self.values += 1

    def remove(self,val):
        h = self.hash_(val)
        self.table[h].remove(val)
        self.values -= 1

    def enlarge(self):
        # when too many values, enlarge table vertically
        return "todo"
    
    def make_smaller(self):
        # when too many values, make smaller table vertically
        return "todo"
    