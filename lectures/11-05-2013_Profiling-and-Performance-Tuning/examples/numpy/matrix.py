import numpy

from decorators import timer

@timer
def offset(matrix, x):
    """add x to all values in matix"""
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            matrix[i][j] += x

@timer
def numpy_offset(matrix, x):
    matrix += x

N=3000

data = [[x for x in xrange(N)] for y in xrange(N) ]

numpy_data = numpy.array(data)

offset(data, 10)
numpy_offset(numpy_data, 10)

print data[4][4]
print numpy_data[4][4]
# print data
