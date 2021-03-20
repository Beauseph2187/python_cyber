#You can convert a range directly into a list by using the list() function.

numbers = list(range(1, 6))
print(numbers)

#You can also use the range() function to tell Python to skip numbers
#in a given range by passing a third argument to a range.

even_numbers =list(range(2 , 11, 2))
print(even_numbers)