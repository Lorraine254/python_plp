# In an instance where you want to store complex information

# Data structure: allows you to organize and arrange your data to perform 
# operations on them

# Built in data structures ---> non-primitive data structures
## List
## Dictionary
## Tuple
## Set

# User defined data structures
## Stacks
## Queues
## Trees

# Each data structure can be designed to solve a particular problem or optimize a current solution to make it much more perfomant.


# Mutability and Immutability

#==============================================================================
## Mutability - can be modified that is data can be changed, updated or deleted i.e 
### List 

# Creating a list
numbers = [1,2,3]
print(numbers)

# Empty list
my_list = []

# List with mixed data types
my_list = [1, "Hello", 3.4]

# Accessing python list items ---> indexing starts from o
print(my_list[1])

# Slicing a list
my_list=["p",'r','o','g','r','a','m','i']

print(my_list[0:4]) #p,r,o,g
print(my_list[5:]) #a, m, i
print(my_list[:])
print(my_list[-1:-3])

# Adding elements to a list ---> append
#append() ---> methods adds an item at the end of the list
numbers = [21, 34, 54, 12]

print(f"Before append:{numbers}")

numbers.append(32)
print(f"After append:{numbers}")

#extend() ---> adds all items one list to another

prime_numbers = [2,3,5]
even_numbers = [4,6,8]
prime_numbers.extend(even_numbers)
print(prime_numbers)

# change list items
prime_numbers[2]='C'
print(prime_numbers)

# Removing an item from a list
del prime_numbers[2]
print(prime_numbers)

for i in prime_numbers:
    print(i)

# list comprehension ---> shorter syntax when you want to create a new list based on 
# the values of an existing list
fruits = ['apple','banana','cherry','kiwi','mango']

###[expression for item in iterable if condition == True]

newlist = [x for x in fruits if 'a' in x]
print(newlist)

#======================================================================================
## Immutability - will not allow modification once the  data has been set.
### Tuple

## Can contain different data types
var1="hello",
print(var1)

var2 = ("Simulation",)
print(var2)

var3 = ("hello", 1, "Simulation")
print(var3)
print(var3[-1])

my_tuple = ('a','p','l','e','p')
print(my_tuple.count('p'))
print(my_tuple.index('p'))

#========
#==================================================================================
## Dictionary ---> is an ordered collection; contains key and value pairs
# We can have keys and values of different data types
capital_city = {"Nepal":"Kathmandu","Italy":"Rome","England":"London"}
print(capital_city)

# Adding elements to a dictionary
capital_city['Japan'] = "Tokyo"
print(capital_city)

# Changing value of a dictionary
capital_city['Japan'] = "Nairobi"
print(capital_city)

# Accessing elements of a dictionary
student_id ={111: "Eric",112: "Kyle",113:"Lovey"}
print(student_id[112])

# Removing elements from a dictionary
del student_id[112]
print(student_id)

# Dictionary methods
print(student_id.keys())
print(student_id.values())
print(student_id.clear())
print(student_id)


## Membership Test
### We can test if a key is in a dictionary or nont
squares = {1 : 1, 3:9, 5:25, 7:49,9:81}
print(1 in squares)
print(1 not in squares)

## Iterating through a dictionary
for i in squares:
    print(squares[i])

#====================================================================================================
## Set ---> 
# is a collection of unique data, can't contain duplicates
# Can contain different data types
# Cannot contain mutable elements like lists, sets or dictinaries

student_id = {112, 113, 114,115, 116,117}
print(student_id)

mixed_set={"Hello",101, -2, "Bye"}
print(mixed_set)

# creating an empty set
empty_set = set()
empty_dictionary = {}

print(empty_set)
print(empty_dictionary)

# Sets are mutable, but are unordered
# Thus we cannot access or change an element of a set using indexing or slicing

# Add items to a set
numbers = {21,34,54,12}
print(numbers)
numbers.add(32)
print(numbers)

# Update Python set --> is used to update the set with items of other collection
# types
companies = {'Lacoste','Ralph Lauren'}

tech_companies = ['apple','google','apple']
companies.update(tech_companies)
print(companies)

# Remove an element from a set
companies.discard('apple')
print(companies)


# Python Set Operations
A = {1,3,5}
B = {0,2,4}
print("Union using |:", A|B)
print("Union using union():", A.union(B))
