import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)



# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)
# Save the DataFrame to an Excel file
#df.to_excel('output.xlsx', index=False)
# Save the DataFrame to a JSON file
df.to_json('output.json', orient='records', lines=True)
# Save the DataFrame to a Parquet file
df.to_parquet('output.parquet', index=False)
# Save the DataFrame to a Feather file
df.to_feather('output.feather')
# Save the DataFrame to a Stata file
df.to_stata('output.dta', write_index=False)
# Save the DataFrame to an HDF5 file
df.to_hdf('output.h5', key='df', mode='w', format='table')
# Save the DataFrame to a clipboard
df.to_clipboard(index=False)
# Save the DataFrame to a SQL database (example using SQLite)
import sqlite3

conn = sqlite3.connect('output.db')
df.to_sql('data', conn, if_exists='replace', index=False)
conn.close()    

