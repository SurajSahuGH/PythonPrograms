
data = [
{'name': 'Alice', 'age': 25},
{'name': 'Bob', 'age': 30},
{'name': 'Charlie', 'age': 35}
]

compress_data = {
'name': ['Alice', 'Bob', 'Charlie'],
'age': [25, 30, 35]
}


# converting data to compress_data

# with two loops
# cdt = {}
##for col in data[0]:
##    cdt[col] = []
##    for row in data:
##        cdt[col].append(row[col])


# with dictionary comprehension & list compre
cdt = {col:[row[col] for row in data] for col in data[0]}
print(cdt)

# converting compress_data back to data
dt = [dict(zip(compress_data.keys(), row)) for row in zip(*compress_data.values())]
print(dt)

