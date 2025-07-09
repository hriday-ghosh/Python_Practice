# Pandas Basic and Advanced Syntaxes Explained Simply

import pandas as pd  # Import pandas

# ---------------- BASIC ----------------

# 1. Create DataFrame from Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 95],
    'Passed': [True, True, False]
}
df = pd.DataFrame(data)  # Create DataFrame
print(df)  # Show full table

# 2. Read CSV / Excel
# df_csv = pd.read_csv('file.csv')  # Read CSV file
# df_excel = pd.read_excel('file.xlsx')  # Read Excel file

# 3. Write CSV / Excel
df.to_csv('output.csv', index=False)  # Save to CSV (no index)
df.to_excel('output.xlsx', index=False)  # Save to Excel

# 4. Inspect Data
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.shape)  # Rows and columns
print(df.columns)  # List of column names
print(df.info())  # Summary with types
print(df.describe())  # Stats for numeric columns

# 5. Select Columns & Rows
print(df['Name'])  # Select single column
print(df[['Name', 'Score']])  # Multiple columns
print(df.loc[0])  # Row by index (label-based)
print(df.iloc[1])  # Row by position (integer-based)

# 6. Filtering Data
print(df[df['Score'] > 85])  # Filter rows with Score > 85
print(df[(df['Score'] > 85) & (df['Passed'] == True)])  # Combine conditions

# 7. Add / Update / Delete Columns
df['Grade'] = ['B', 'A', 'A+']  # Add new column
print(df)
df['Score'] = df['Score'] + 5  # Update column
print(df)
del df['Passed']  # Delete column
print(df)

# 8. Sorting Data
print(df.sort_values(by='Score', ascending=False))  # Sort by Score

# 9. Handling Missing Data
df2 = pd.DataFrame({
    'A': [1, None, 3],
    'B': [4, 5, None]
})
print(df2.isnull())  # Check missing values
print(df2.fillna(0))  # Replace NaN with 0
print(df2.dropna())  # Drop rows with any NaN

# 10. GroupBy
print(df.groupby('Grade')['Score'].mean())  # Average Score per Grade

# ---------------- ADVANCED ----------------

# 11. Merge / Join
students = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
scores = pd.DataFrame({
    'ID': [1, 2, 3],
    'Score': [90, 85, 80]
})
merged = pd.merge(students, scores, on='ID')
print(merged)  # Merged by common column 'ID'

# 12. Pivot Table
pivot = df.pivot_table(values='Score', index='Grade', aggfunc='mean')
print(pivot)  # Average score per grade

# 13. Apply Function
def bonus(score):
    return score + 10

df['Bonus'] = df['Score'].apply(bonus)  # Apply function to column
print(df)

# 14. Export Filtered Data
high_scores = df[df['Score'] > 90]
high_scores.to_csv('high_scores.csv', index=False)  # Save filtered data

# 15. Reset and Set Index
df_reset = df.reset_index(drop=True)  # Reset index
df_indexed = df.set_index('Name')  # Set column as index
print(df_indexed)

# Now you can analyze, transform, and export data using pandas!
