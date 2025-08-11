# Creat an empty list
my_list = []
print("Confirming the data type:")
print(type(my_list))
print(f"Confirming the list is empty: {my_list}")
print("==="*26)

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"Appending elements to the empty list: {my_list}")
print("==="*26)

# Insert the value at the second position in the list
my_list.insert(1,15)
print(f"Inserting the value at the second position: {my_list}")
print("==="*26)

# Extend the list with another list
list2=[50,60,70]
my_list.extend(list2)
print(f"Extending the list with another list: {my_list}")
print("==="*26)

# Remove the last item in the list
del my_list[-1]
print(f"Removing the last item in the list: {my_list}")
print("==="*26)
# Sort list in ascending order
my_list.sort()
print(f"Sorting the list in ascending(S-L) order: {my_list}")
print("==="*26)

# Find and print the index of the value 30 in my_list
print(f"Index of the value 30 is: {my_list.index(30)}")
print("==="*26)
