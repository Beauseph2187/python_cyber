from guess import guessing

choices = {
    "guess": guessing,
    "exit": exit,
    "also": exit,
}

while True:
    print("Options are:\nexit\nguess\nalso")
    option = input("What to do: ")
    if result:= choices.get(option):
        result()
        exit()
    else:
        print("invalid input")

