#Copying Lists
#I can copy entire lists by omitting the first and second index. [:]

my_foods = ['steak', 'sushi', 'roast chicken']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("n\My friend's favorite foods are:")
print(friend_foods)

#You can add items to list with .append()

my_foods = ['steak', 'sushi', 'roast chicken']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("n\My friend's favorite foods are:")
print(friend_foods)

#Copying a list does not work if you do not use a slice!!
#Ex: my_foods = friend_foods << this just results in the lists
#being set equal to eachother, not copied!!