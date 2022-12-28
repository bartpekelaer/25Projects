import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again, to low")
        elif guess > random_number:
            print("Guess again, too high")
    print(f"Correct! the number was {random_number}")


if __name__ == "__main__":
    guess(20)
