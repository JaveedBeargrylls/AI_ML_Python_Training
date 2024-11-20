import pandas as pd  # Import the pandas library for data manipulation

# Read the CSV file into a DataFrame. The 'r' in front of the string makes it a raw string literal,
# so backslashes in the path are treated literally.
data = pd.read_csv(r"Day02\insurance.csv")

# Print the type of the 'data' object to confirm it's a pandas DataFrame
print(type(data))  # <class 'pandas.core.frame.DataFrame'> indicates that data is a DataFrame

# Print the shape of the DataFrame, which returns a tuple with the number of rows and columns
print(data.shape)  # (rows, columns)

# Display the first 5 rows of the DataFrame. By default, `head()` shows the first 5 rows.
print(data.head())  # Default is 5 rows, useful for getting a quick preview of the data

# Display the last 5 rows of the DataFrame. `tail()` is similar to `head()`, but shows the last 5 rows.
print(data.tail())  # Shows the last 5 rows, useful for checking the end of the data

# To get a custom number of rows, you can specify the number as an argument to `head()` or `tail()`.
# This will display the first 2 rows of the DataFrame.
print(data.head(2))  # Show the first 2 rows

# This will display the last 8 rows of the DataFrame.
print(data.tail(8))  # Show the last 8 rows

# The `info()` function provides a concise summary of the DataFrame, including:
# - The total number of entries (rows),
# - The number of non-null entries in each column,
# - The datatype of each column.
print(data.info())  # Useful for checking data types and null value counts

# Access a column by its name. This returns a pandas Series, which is essentially a single column.
print(data.age)  # Accesses the 'age' column. It's a shorthand for data['age']

# The __dir__ method gives a list of all the attributes and methods available for the DataFrame.
# It's a reflection method used for introspection.
print(data.__dir__)  # List all available attributes and methods of the DataFrame object
print("DATA FRAME\n"+str(data.__dir__))

# Access a column using bracket notation (recommended for flexibility). Bracket notation works for column names
# that may not be valid Python identifiers or contain spaces.
print(data['age'])  # Accesses the 'age' column using bracket notation

# You can access multiple columns by passing a list of column names inside double brackets.
print(data[['age', 'bmi']])  # Accesses both 'age' and 'bmi' columns

# You can also use `.head()` on the subset of columns to preview only those columns.
print(data[['age', 'bmi']].head(2))  # Show the first 2 rows for 'age' and 'bmi' columns

# The `describe()` method generates descriptive statistics of the DataFrame. By default, it will:
# - Show statistics for numerical columns (e.g., count, mean, std, min, 25%, 50%, 75%, max).
# - It only includes numeric columns unless `include='all'` is specified to include categorical columns as well.
print(data.describe())  # Display summary statistics for numerical columns

# Using describe() with include='all' to get descriptive statistics for both numerical and categorical columns.
# For numerical columns, it will show:
# - count: Number of non-null entries
# - mean: The average (mean) value
# - std: Standard deviation, a measure of spread
# - min: The minimum value
# - 25%, 50%, 75%: The 25th, 50th (median), and 75th percentiles (quartiles)
# - max: The maximum value
#
# For categorical columns, it will show:
# - count: Number of non-null entries
# - unique: The number of unique values
# - top: The most frequent (mode) value
# - freq: The frequency of the most frequent value

print(data.describe(include='all'))  # Print the summary statistics for all columns (both numerical and categorical)

# 25th Percentile (Q1) - The "lower quartile" or the 1st quartile:
# This is the value that separates the **lowest 25%** of the data.
# It means that 25% of the data points are below this value, and 75% are above.
# It's the point where the **lower quarter** of the data ends.
# This helps you understand the lower bound of your data.

# 50th Percentile (Median) - The "middle" of the data:
# The median is the value that divides the data into two equal halves.
# 50% of the data points are below this value and 50% are above.
# It represents the **middle** of your data, and it is useful for understanding the **central tendency**.
# It is less sensitive to outliers compared to the mean.

# 75th Percentile (Q3) - The "upper quartile" or the 3rd quartile:
# This is the value that separates the **lowest 75%** of the data from the remaining 25%.
# It means that 75% of the data points are below this value, and 25% are above.
# It's the point where the **upper quarter** of the data begins.
# This helps you understand the upper bound of your data.

# Visual representation of quartiles: Box Plot (Box-and-Whisker Plot)
# A box plot can help visualize these quartiles:
# - The **box** shows the range between the 25th (Q1) and 75th (Q3) percentiles.
# - The **line inside the box** represents the 50th percentile (Median).
# - The **whiskers** extend to the minimum and maximum values, and they show the range of the data.

