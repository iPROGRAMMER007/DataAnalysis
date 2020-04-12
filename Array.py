import numpy as np
#from numpy import *

import time
import sys

# one dimensional array
a = np.array([1,2,3,4,5])

#Two dimensional array

b = np.array([(1,2,3,4,5),(6,7,8,9,10)])

#print(b)
#print(a)

# Numpy has less memory then list


s = range(1000)
print(sys.getsizeof(1)*len(s))

print(sys.getsizeof(1000))

d = np.arange(1000)
print(d)
print(sys.getsizeof(d))
print(d.size*d.itemsize)


#Numpy is more convenient then list

size = 1000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

#for list
start = time.time()
result = [(x,y) for x,y in zip(l1,l2)]
print('Time for list'+str((time.time() - start)*1000))

#for numpy array

start = time.time()
result = a1 + a2
print('Time for list'+str((time.time() - start)*1000))















