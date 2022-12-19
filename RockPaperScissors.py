import random


def compare(value1, value2):
    value1 = value1.lower().strip()
    if value1 == value2:
        print("You tied")
    elif value1 == "rock":
        if value2 == "paper":
            print("You Lose")
        else:
            print("You win")
    elif value1 == "paper":
        if value2 == "scissor":
            print("You Lose")
        else:
            print("You Win")
    elif value1 == "scissor":
        if value2 == "rock":
            print("You Lose")
        else:
            print("You Win")

    else:
        print("NOPE")


def game():
    a = input("rock,paper,scissor: ")
    b = random.choice(["rock", "paper", "scissor"])
    print(f"Your choices is {a}, and your opponents choice is {b}")
    compare(a, b)


while True:
    game()
