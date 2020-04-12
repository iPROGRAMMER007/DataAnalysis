import matplotlib.pyplot as pop

x1 = [5,10,15,20]
y1 = [10,20,67,89]

x2 = [78,90,56,34]
y2 = [23,78,66,99]


pop.bar(x1,y1,label = 'Example one',color = 'red',linewidth = 10)
pop.bar(x2,y2,label = 'Example two',color = 'green')

pop.legend()
pop.title('Bar graph')
pop.xlabel('X-axis')
pop.ylabel('Y-axis')

pop.show()







