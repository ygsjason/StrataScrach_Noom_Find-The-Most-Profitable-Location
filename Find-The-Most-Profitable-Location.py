# Import your libraries
import pandas as pd

# Start writing code
signups
transactions

# Method_1
df1 = signups
df2 = transactions
#df = pd.merge(df1, df2, how = 'left', on = ['signup_id'])
df1['d'] = (df1.signup_stop_date - df1.signup_start_date).dt.days

# Calculate the av_d from df1 for locations
df3 = df1.groupby('location')['d'].mean().reset_index()

# Get the av_r from df2 for locations
# df2 need to add location field. signup_id is PK bt df1 and df2
df4 = pd.merge(df2, df1, on = 'signup_id', how = 'left')
df5 = df4.groupby('location')['amt'].mean().reset_index()

# Join df5 and df3 to get the ration field.
df6 = pd.merge(df3, df5, on = 'location', how = 'left')
df6['r'] = df6.amt/df6.d
df6.sort_values(['r'], ascending = False)

## Method_2
# Calculate the duration of signups
signups['duration'] = (signups['signup_stop_date'] - signups['signup_start_date']).dt.days
# Get the average duration
avg_dur_df = signups.groupby(by = ['location'], as_index = False).mean()
 
# Get the location_id from the signups dataset
merged_df = pd.merge(left = transactions, right = signups[['signup_id', 'location']], 
on = 'signup_id', how = 'left')
# Summarize by location
trans_df = merged_df.groupby(by = ['location'], as_index = False).mean()
 
# Merge the dataframes keeping only the relevant columns
final_merged_df = pd.merge(avg_dur_df[['location', 'duration']], trans_df[['location', 'amt']], on = 'location', how = 'inner')
 
# Calculate ratio, sort and submit.
final_merged_df['ratio'] = final_merged_df['amt'] / final_merged_df['duration']
final_merged_df.sort_values(by = ['ratio'], ascending = False)
