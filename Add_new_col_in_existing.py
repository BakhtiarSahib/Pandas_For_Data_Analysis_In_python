import pandas as pd

data = {

 "Name" : ['sumaya','rizvi','mahad','mousia','suma'],
 "Age":[10,20,30,40,50],
 "salary" : [50000,60000,52000,68000,72000],
 "perfomance_score":[45,67,23,48,78]

}

df= pd.DataFrame(data)
print(df)
# Adding a new column 'Experience' with default value 5
df['Bonus'] = 0.1 * df['salary']
print(df)

# Adding a new column  in a specific position
df.insert(2, 'ID', [1, 2, 3, 4, 5])
print(df)   
