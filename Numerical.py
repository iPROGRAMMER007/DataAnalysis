import numpy as np
import matplotlib.pyplot as plt

a = np.array([(1,2,3,4),(5,6,7,8)])
b = np.array([(1,2,3,4),(9,8,7,6)])

print(a+b)

print(a*b)
print(a/b)
print(a-b)
print('*'*50)
#Put one over another

print(np.vstack((b,a)))
print('*'*50)

print(np.hstack((a,b)))
print('*'*50)
#Convert into single list or into a single line

#print(a.ravel())

#Plot sin graph and cosine graph

'''
x  = np.arange(0,3*np.pi,0.1)
#y = np.sin(x)
#y = np.cos(x)
y = np.tan(x)
plt.plot(x,y)
plt.show()

'''
#Exponential function and logarithmic function

ar = np.array([1,2,3,4])
print(np.exp(ar))
print('*'*50)
print(np.log(ar))
print('*'*50)
print(np.log10(ar))









