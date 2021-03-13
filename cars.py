#Sort a list by alphabetical order by using .sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#Sort cars in reverse alphabetical order
#by setting reverse=True

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Sort lists temporarily by using the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#Printing lists in reverse order
#Just reverse, not reverse alphabetically

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Finding length of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))