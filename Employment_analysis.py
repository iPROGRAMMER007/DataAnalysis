
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

country = pd.read_csv('C:\\Users\MD.IRSHAD\\PycharmProjects\\Data_Analysis\\employment.csv',index_col=0)

country = country.set_index(['Country Code'])
#print(country.head(5))
country = country.head(10)
print(country)

sd = country.reindex(columns = ['2011','2012'])
#print(sd.head(5))

db =  sd.diff(axis=1)

db.plot(kind = 'bar')
plt.show()


