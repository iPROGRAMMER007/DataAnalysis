import pandas as pd

#Merging

df1 = pd.DataFrame({'HPI':[80,90,70,60],'Int_rate':[2,1,2,3],'IND_GDP':[50,45,45,67]},
                   index = [2001,2002,2003,2004])


df2 = pd.DataFrame({'HPI':[80,90,70,60],'Int_rate':[2,1,2,3],'IND_GDP':[50,45,45,67]},
                   index = [2005,2006,2007,2008])

merge_frame  = pd.merge(df1,df2)

#print(merge_frame)

merge_frame1 = pd.merge(df1,df2 , on  = 'HPI')

print(merge_frame1)




