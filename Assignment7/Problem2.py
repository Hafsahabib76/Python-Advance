import pandas as pd

# Set the csv file path (change with the actual path of the file)
file_path = r"C:\Users\Desktop\result.csv"

# Reading the student result CSV file
marks_total_percentage_df = pd.read_csv(file_path)

# Display the first few rows of the student marks dataframe
print("Head:")
print(marks_total_percentage_df.head())

# Display the last few rows of the student marks dataframe
print("\nTail:")
print(marks_total_percentage_df.tail())

# Display information about the student marks dataframe
print("\nInfo:")
print(marks_total_percentage_df.info())

# Descriptive statistics of the student marks dataframe
print("\nDescribe:")
print(marks_total_percentage_df.describe())

# Column selection for student marks dataframe
print("\nColumn Selection:")
selected_columns_total_percentage = marks_total_percentage_df[['StudentName', 'Percentage']]
print(selected_columns_total_percentage)