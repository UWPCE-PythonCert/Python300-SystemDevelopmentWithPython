import random

def my_iterator():
    data = range(10)
    random.shuffle(data)
    for x in data:
        if x == 9:
            raise StopIteration
        else:
            yield x


for x in my_iterator():
    print x
