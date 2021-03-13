motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Inserting something into a list(must specify location)

motorcycles.insert(0, 'ducati')
print(motorcycles)

#Using the .pop method. (.pop shows the last thing in a list)
#unless you specify where in the list you want.

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcyle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#Removing items by value

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#Avoiding index errors
#Python starts at 0, not 1, so below will result in error.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

#Use [-1] when you want to access last item in list.
#However, if you use [-1] for empty list, it will error.