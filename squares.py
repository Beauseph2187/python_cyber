#You can create almost any set of numbers in Python
#With the range function range() ex: square numbers

squares = []
for value in range (1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

#You can write the code more concisely by omitting temp valuable square

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)    

#List comprehensions allow me to list the same numbers
#but in just one line of code.

squares = [value**2 for value in range(1, 11)]
print(squares)