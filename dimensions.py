#Tuples are immutable(unchangeable) lists.
#You use parenthesis instead of square brackets for tuples.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Changing the dimensions results in a type error
#Ex: dimensions[0] = 250

#In order to define a tuple with one element
#you must use a trailing comma. Ex: my_t = (3,)

#You can loop through values in a tuple using a for loop

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#Since you can't modify tuples, you can assign a new value
#to a variable that represents a tuple.

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("n\Modified dimensions")
for dimension in dimensions:
    print(dimension)


#Use tuples when you want to store values that should
#not be changed throughout the entire life of a program.