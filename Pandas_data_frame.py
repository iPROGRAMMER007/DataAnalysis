import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'Student':['Irshad','Vikash','Akhilesh','Dhiraj','Mukhiya'],'Marks':[89,90,78,99,88]}
data_frame = pd.DataFrame(data)
print(data_frame)
print('*'*50)

#Slicing the row using head() function
print(data_frame.head(2))
print('*'*50)
print(data_frame.tail(3))












































