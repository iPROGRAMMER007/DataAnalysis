import pandas as pd

# Data munging means converting one type of file to other types of file

data = pd.read_csv('C:\\Users\MD.IRSHAD\\PycharmProjects\\Data_Analysis\\bikes.csv')  #This is from pycharm Charm
#data = pd.read_csv('C:\\Users\\MD.IRSHAD\\Data_Analysis\\Master Data Analysis with Python - Intro to pandas\\bikes.csv') // This is from outer file
data.to_html('bikes.html')

#print(data.head())




