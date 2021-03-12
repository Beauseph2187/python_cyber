# List 
"""
[] <- This is an empty list
[1, 2, 3] <- This is a list with 3 elements

[...]
[<>, <var / data>...] 
"""

# students is now an empty list
students = []

# This is a list with many things
ratings = [1, 4, 3, 2, 3, 5, 1, 5, 4, 5]
ratings.append(4)
# len() <- the number of things in a list
print(len(ratings))

# Getting something out of a list
print(ratings[5])

# Dict
movie = {}

person = {
    "name": "Beau",
    "age": 25,
    "fav_food": "Steak"    
}

print(person)
print(person["name"])
print(person["age"])

computer = {
    "host":"Swift", # this is kinda like host  = "Swift"
    "ip": "192.168.0.2",
    "port": 22
}

print
(f"{computer['host']}@{computer['ip']}:{computer['port']}"
)

f_name ="Beau's"