#!/usr/bin/env python

class FibIterator(object):

    def __init__(self):
        self.data = [0,1,1,2,3,5,8,13,21]
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i >= len(self.data):
            raise StopIteration

        value = self.data[self.i]
        self.i += 1
        return value

iter = FibIterator()
for x in iter:
    print x
