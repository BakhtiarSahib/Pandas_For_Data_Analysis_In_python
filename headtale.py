import pandas as pd

# Read data from CSV file
df = pd.read_csv('/Users/hpnnpq/Documents/python/pandas/sales_data_sample.csv', encoding="latin1")
# Display the DataFrame
print(df)       



# Display the first few rows of the DataFrameprint(df.head())
print(df.head())            
# Display the last few rows of the DataFrame
print(df.tail())
# Display the shape of the DataFrame
print(df.shape)
# Display the columns of the DataFrame
print(df.columns)
# Display the data types of the columns
print(df.dtypes)
# Display the summary statistics of the DataFrame
print(df.describe())
# Display the unique values in a specific column
print(df['Product line'].unique())
# Display the number of unique values in a specific column
print(df['Product line'].nunique())
# Display the value counts of a specific column
print(df['Product line'].value_counts())
# Display the first 10 rows of a specific column
print(df['Product line'].head(10))
# Display the last 10 rows of a specific column
print(df['Product line'].tail(10))
# Display the first 10 rows of the DataFrame
print(df.head(10))
# Display the last 10 rows of the DataFrame
print(df.tail(10))
# Display the first 10 rows of the DataFrame with specific columns
print(df[['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns
print(df[['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))          

# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))

# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))      
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total']
> 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of
# the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))

# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific                   
# columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))  
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
# Display the last 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].tail(10))
# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total']                    
         
> 100][['Invoice ID', 'Product line', 'Total']].head(10))


# Display the first 10 rows of the DataFrame with specific columns and a condition
print(df[df['Total'] > 100][['Invoice ID', 'Product line', 'Total']].head(10))
