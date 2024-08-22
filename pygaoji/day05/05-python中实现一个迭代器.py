class MyIterator:
    def __init__(self,start,end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for i in MyIterator(1,10):
    print(i)