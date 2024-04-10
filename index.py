import pandas as pd

# Read data from CSV file
df = pd.read_csv('SBIN_Data.csv')

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Filter the DataFrame to include only the rows for the last 5 days
end_date = df['Date'].max()
start_date = end_date - pd.Timedelta(days=5)
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Exclude weekends from the filtered DataFrame
filtered_df = filtered_df[filtered_df['Date'].dt.dayofweek < 5]

# Sort the filtered DataFrame by Time and Volume in descending order
rank = filtered_df.query('Time == "09:40:00"').sort_values('Volume', ascending=False)

# Add a new column 'Rank' to the DataFrame
rank['Rank'] = range(1, len(rank) + 1)

# Print the DataFrame
print(rank)



