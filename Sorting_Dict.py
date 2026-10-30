# Key, Value of the dictionary defined
d = {'watermelon': 1, 'apple': 2, 'banana': 3}        

# Sort based on Keys
val_based = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
# item[1] represents the sorting based on value

# Sort based on Values
val_based_rev = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

# Print sorted dictionary
print(val_based)
print(val_based_rev)
