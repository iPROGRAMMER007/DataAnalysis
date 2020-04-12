import numpy as np

a = np.array([(1,2,3,4),(5,6,7,8),(9,0,10,11),(12,13,14,15)])
print(a)

'''
#Check dimension of array
print(a.ndim)

#Check the size of an array
print(a.size)

#Check the shape of the array
print(a.shape)

#Check item size
print(a.itemsize)
#Check data type
print(a.dtype)

#change the shape of the array
print(a.reshape(2,8))
print(a.reshape(8,2))

'''
b = np.array([(1,2,3,4),(9,8,7,6)])

'''
print(b)
print(b.reshape(4,2))

#Slicing the element means extracting the desired elements
#Left side row and right side column
print(a[2,0])
print(b[1,2])

print(a[0:,2])
print('*'*50)
print(a[0:2,3])
print('*'*50)
print(a[0:3])
print('*'*50)
print(a[2:4])
print('*'*50)
#print(a[0:3],4)

#linespaceing means how many count between two numbers
c = np.linspace(1,10,20)
print(c)

#Find minimum maximum and sum

print(a.min())
print(a.max())
print(a.sum())

#Axis related things

print(b.sum(axis=0))
print(b.sum(axis=1))
'''

#Find square root of each element

print(np.sqrt(b))
print(np.sqrt(b[1,1]))

#Find standard deviation

print('Standard deviation = '+str(np.std(b)))






















