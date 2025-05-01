class Counter:
    def __init__(self, start,end):
        self.curr = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr > self.end:
            raise StopIteration
        value = self.curr
        self.curr += 1
        return value
    
counter = Counter(1, 5) 

# iterator = iter(counter)
# while True:
#     try:
#         curr_elem = next(iterator)
#         print(curr_elem )
#     except StopIteration as e:
#         print("Error : ", e)
#         break
#  The above comment things happenf when we write for loop on the iterator

# for curr_elem in counter:
#     print(curr_elem)
    
    
#  we can do the above using generator in simpler way


def counter(start, end):
    while start <= end:
        yield start
        start += 1

for curr_value in counter(1, 12):
    print(curr_value)
