import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style





style.use('fivethirtyeight')

df1 = pd.DataFrame({'Int_rate':[2,1,2,3],'IND_GDP':[50,45,45,67]},
                   index = [2001,2002,2003,2004])

df2 = pd.DataFrame({'Low_Tier_HPI':[50,45,67,34],'Unemployment':[1,2,5,6]},
                   index = [2001,2003,2004,2005])


joining = df1.join(df2)

#print(joining)

# Indexing

df = pd.DataFrame({'Day':[1,2,3,4,5],'Visitors':[200,230,300,350,400],'Bounce_rate':[25,45,50,34,30]})
#df.set_index('Day',inplace=True)

#Changing column header (Column name)

df = df.rename(columns={'Visitors':'Users'})





print(df)
#df.plot()
#plt.show()


