
import  pandas as pd

ds= pd.read_excel('data.xlsx' , names=['c1' , 'c2' , 'c3' ,'c4'])

ds.index = ['S1' , 'S2' , 'S3' ]

# print(ds)

# print(ds.shape)

#print(ds.dtypes) # str as Object

# print(ds.describe()) # summarization about data

print(ds.loc['S2'])
print(ds.iloc[0])