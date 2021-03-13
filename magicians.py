#List looping

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#Doing more things in a For loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n" )

    print("Thank you, everyone. That was a great magic show!")

    #Avoiding Indentation Errors
    #Python will tell me that I need to indent the print function


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)    

#Forgetting to Indent Additional Lines
#Python does not report the error due to the previous indent
#This is called a logical error

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

#You do not need to indent print calls that are not part of a loop.
#Indenting code after a loop causes it to print once
#Sometimes Python will call error, otherwise logical error

#Forgetting colon

magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)

#Forgetting the colon causes a syntax error. 