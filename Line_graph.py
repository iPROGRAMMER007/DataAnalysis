from matplotlib import pyplot as pyp
from matplotlib import style

#from matplotlib import *

style.use('ggplot')

#Simple means default lines
'''
x = [3,5,8,9]
y = [7,2,9,4]

pyp.plot(x,y)
pyp.show()
'''
#Colorful lines

x1 = [9,6,3,0]
y1 = [1,5,9,14]

x2 = [10,20,30,40]
y2 = [30,60,90,120]

pyp.plot(x1,y1,'red',label = 'line one',linewidth = 3)
pyp.plot(x2,y2,'green',label = 'line two',linewidth = 3)


pyp.title('Epic info')
pyp.xlabel('X-label')
pyp.ylabel('Y-label')

pyp.legend()

pyp.grid(True,color = 'k')

pyp.show()

