import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [5,4,6,8,1,7,3,0,1]

plt.scatter(x, y, label='ckitscat', color='red')

plt.title('Scatter')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()






