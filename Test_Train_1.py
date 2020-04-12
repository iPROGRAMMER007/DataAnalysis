import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Linear Regression

df = pd.read_csv("C:\\Users\\MD.IRSHAD\\PycharmProjects\\Excel_Files\\CarPrice.csv")

#print(df.head())

# # Car Mileage vs Sell Price
# a = plt.scatter(df["Milage"], df["Sell Prices(s)"])
# plt.show(a)
# # Car vs Sell price
# b = plt.scatter(df["Age(yrs)"], df["Sell Prices(s)"])
#
# plt.show(b)

x = df[["Milage", "Age(yrs)"]]
y = df["Sell Prices(s)"]

# print("Independent variables : \n")
# print(x)
# print("Dependent variables : \n")
# print(y)

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
#print(x_test)

linear_reg = LinearRegression()

# fit() function is used to train model
linear_reg.fit(x_train, y_train)
print(linear_reg.predict(x_test))
# Score() function is to check the accuracy of trained model
accuracy = linear_reg.score(x_test, y_test)
#print(accuracy)
print(y_test)

print("Accuracy : ", accuracy)















