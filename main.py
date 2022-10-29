
import  pandas as pd

ds= pd.read_excel('data.xlsx' , names=['c1' , 'c2' , 'c3' ,'c4' , 'c5'])

ds.index = ['S1' , 'S2' , 'S3' , 'S4' , 'S5']

# print(ds)

# print(ds.shape)

#print(ds.dtypes) # str as Object

# print(ds.describe()) # summarization about data

# print(ds.loc['S2'])
# print(ds.iloc[0])

# print(ds.loc[ : ,'c2']) # from start to end -1 # slicing

#-----------------------------------------------
# valid Emails

correctEmails = []

for p in ds.loc[: , 'c5']:
    if str(p).endswith('com') and str(p).lower() != 'nan' :
        correctEmails.append(p)
    else:
        correctEmails.append('Not Valid Email')

# for i in correctEmails:
#     print(i)


cleandEmails = pd.DataFrame({'Emails':correctEmails})

print(cleandEmails)

cleandEmails.index = ['E1' , 'E2' , 'E3' , 'E4' , 'E5']

cleandEmails.to_excel("correctEmails.xlsx")