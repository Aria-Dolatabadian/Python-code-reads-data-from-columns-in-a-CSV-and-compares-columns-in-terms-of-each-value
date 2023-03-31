import pandas as pd

# Read data from CSV file
data = pd.read_csv('test.csv')

# Extract values from columns
column1_values = data['cl1']
column2_values = data['cl2']
column3_values = data['cl3']
column4_values = data['cl4']
column5_values = data['cl5']
column6_values = data['cl6']
column7_values = data['cl7']
column8_values = data['cl8']
column9_values = data['cl9']
column10_values = data['cl10']


# Count occurrences of each value in column1
column1_value_counts = column1_values.value_counts()
print(column1_value_counts)
# Count occurrences of each value in column2
column2_value_counts = column2_values.value_counts()
print(column2_value_counts)
# Count occurrences of each value in column3
column3_value_counts = column3_values.value_counts()
print(column3_value_counts)
# Count occurrences of each value in column4
column4_value_counts = column4_values.value_counts()
print(column4_value_counts)
# Count occurrences of each value in column5
column5_value_counts = column5_values.value_counts()
print(column5_value_counts)
# Count occurrences of each value in column6
column6_value_counts = column6_values.value_counts()
print(column6_value_counts)
# Count occurrences of each value in column7
column7_value_counts = column7_values.value_counts()
print(column7_value_counts)
# Count occurrences of each value in column8
column8_value_counts = column8_values.value_counts()
print(column8_value_counts)
# Count occurrences of each value in column9
column9_value_counts = column9_values.value_counts()
print(column9_value_counts)
# Count occurrences of each value in column10
column10_value_counts = column10_values.value_counts()
print(column10_value_counts)


# Compare number of occurrences of each value in column1 and column2
for value in column1_value_counts.index:
    column1_count = column1_value_counts[value]
    column2_count = column2_value_counts.get(value, 0)
    if column1_count > column2_count:
        print(f"{value} occurs more often in column1 than in column2")
    elif column1_count < column2_count:
        print(f"{value} occurs more often in column2 than in column1")
    else:
        print(f"{value} occurs equally often in column1 and column2")

print("...........................................................")
# Compare number of occurrences of each value in column7 and column10
for value in column7_value_counts.index:
    column7_count = column7_value_counts[value]
    column10_count = column10_value_counts.get(value, 0)
    if column7_count > column10_count:
        print(f"{value} occurs more often in column7 than in column10")
    elif column1_count < column2_count:
        print(f"{value} occurs more often in column10 than in column7")
    else:
        print(f"{value} occurs equally often in column7 and column10")
