#Slicing lists allows you to work on specific parts of a list.

players = ['charles', 'martina', 'michael', 'florence', 'elli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'elli']
print(players[1:4])

#If you omit the first index, Python starts at beginning of list

players = ['charles', 'martina', 'michael', 'florence', 'elli']
print(players[:4])

#Omitting the second index allows you to work from item to end of list.

players = ['charles', 'martina', 'michael', 'florence', 'elli']
print(players[2:])

#You can also use the [-:] syntax to get the last parts of a list as well.

#Using a slice in a for loop allows for looping subsets of a list.

players = ['charles', 'martina', 'michael', 'florence', 'elli']
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())