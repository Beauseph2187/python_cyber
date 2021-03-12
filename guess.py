def guessing():
    secret = 42
    while True:
        guess = int(input("Guess a number \n> "))
        print(guess)
        if guess == secret:
            print("You have got it!")
            exit()
        elif guess < secret:
            print("You have to guess higher")
        else:
            print("You have to guess lower")


if __name__ == "__main__": # only run the
    guessing()             # following code if I run this file 