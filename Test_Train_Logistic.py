import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

j = 0
titanic = pd.read_csv('Titanic.csv')

#print(titanic.head(10))

# Checking null data in dataframe True means null and False means not null

null = titanic.isnull()
#print(null)

# Sum of all null data for particular column

#sum_null = titanic.isnull().sum()
#print(sum_null)

wrangled_data_frame = titanic.dropna(inplace=True)
#print(wrangled_data_frame)

#sns.heatmap(titanic.isnull(), yticklabels=False, cbar=False)
sum_null = titanic.isnull().sum()
#print(sum_null)

sex = pd.get_dummies(titanic['Sex'],drop_first=True)
passenger_class = pd.get_dummies(titanic['PClass'], drop_first=True)

#print(sex)
#print(passenger_class)

titanic.drop(['PClass', 'Name', 'Sex'], axis=1, inplace=True)
#print(titanic.head(10))

titanic = pd.concat([titanic,sex,passenger_class], axis=1)
#print(titanic.head(10))

# Training and Testing data

x = titanic.drop('Survived', axis=1)
y = titanic['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

logistic_Regression = LogisticRegression()
logistic_Regression.fit(x, y)

accuracy = logistic_Regression.score(x_test, y_test)

print("Accuracy = " + str(accuracy))
predict = logistic_Regression.predict(x_test)
#print(predict)
# for i in predict:
#     if i == 1:
#         j += 1
#         print(j)
# print(len(y_test))


















