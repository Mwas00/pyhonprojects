import pandas as pd

# Load dataset (replace 'your_dataset.csv' with the actual path to your dataset)
df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset to understand its structure
df.head()




# Get information about the dataset, including column names, data types, and non-null counts
df.info()

# Get basic statistical summary (for numeric columns)
df.describe()


# Check for missing values
df.isnull().sum()

# Remove duplicates if needed
df = df.drop_duplicates()

# Handle missing values (example: fill with the mean or drop rows/columns)
df = df.fillna(df.mean())  # Or df.dropna() to drop rows with missing values


# Example: Find correlation between numeric columns
correlation_matrix = df.corr()
print(correlation_matrix)


import matplotlib.pyplot as plt
import seaborn as sns

# Example: Plot a histogram for a numeric column
df['column_name'].hist(bins=20)
plt.title('Histogram of column_name')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Example: Scatter plot to visualize correlation between two columns
sns.scatterplot(x='column1', y='column2', data=df)
plt.title('Scatter Plot between column1 and column2')
plt.show()

# Example: Heatmap of correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()


# Example findings:
print("Key observations:")
print("- The highest correlation is between column1 and column2.")
print("- There is a clear trend where column1 increases as column2 increases.")
print("- The dataset has some missing values in column3, which have been handled by filling with mean values.")
