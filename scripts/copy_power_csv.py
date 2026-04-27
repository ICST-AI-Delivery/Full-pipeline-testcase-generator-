import pandas as pd

# Read the original CSV with special characters in filename
df = pd.read_csv(r'data_files/T_POWER_MANAGEMENT_($0503).csv')

# Remove duplicates
df_clean = df.drop_duplicates()

# Save to new filename
df_clean.to_csv('data_files/T_POWER_MANAGEMENT.csv', index=False)

print(f'Created clean CSV with {len(df_clean)} unique entries')
print('Entries:')
for i, row in df_clean.iterrows():
    print(f'  {i+1}. {row["Image Name"]}')
