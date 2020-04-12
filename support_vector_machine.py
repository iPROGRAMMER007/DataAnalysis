import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()
#print(type(iris))
#print(dir(iris))
#print(iris.feature_names)
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
# print(iris_df.head())
# print(iris.target_names)
# print(iris_df[iris_df.target == 1].head())

iris_df['flower_name'] = iris_df.target.apply(lambda x: iris.target_names[x])
#print(iris_df.head())

# iris_df0 = iris_df[iris_df.target == 0]
# iris_df1 = iris_df[iris_df.target == 1]
# iris_df2 = iris_df[iris_df.target == 2]

# print(iris_df0.head())
# print(iris_df1.head())
# print(iris_df2.head())

# plt.title('Scatter Plot')
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')
# plt.scatter(iris_df0['sepal length (cm)'], iris_df0['sepal width (cm)'], color='green', marker='+')
# plt.scatter(iris_df1['sepal length (cm)'], iris_df1['sepal width (cm)'], color='blue', marker='_')
# plt.scatter(iris_df2['sepal length (cm)'], iris_df2['sepal width (cm)'], color='red', marker='.')
# plt.show()

x = iris_df.drop(['target', 'flower_name'], axis='columns')
#print(x.head())
y = iris_df.target
#print(y.head())
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#print(len(x_train), len(x_test))

model = SVC()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))















































