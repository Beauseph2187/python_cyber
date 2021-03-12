import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
 
# Taking Inputs
upper = int(input("Enter Upper bound:- "))
 
# Generates random number between
# lower limit and upper limit
x = random.randint(lower, upper)
print("\n\tYou have ", 
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the number!\n")
 
# Initializes the number of guesses.
count = 0
 
# For calculating the minimum number of
# guesses, depends upon the range
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # Taking guess as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " tries!")
        # Once guessed, the loop breaks
        break
    elif x > guess:
        print("You guessed too low!")
    elif x < guess:
        print("You guessed too high!")
 
# If guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tThank you for playing!")
 
