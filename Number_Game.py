import random


def game():

    secret_num = random.randint(1, 10)
    attempts = []

    while len(attempts) < 5:

        try:
            guess_num = int(input("Enter a number between 1 and 10: "))
        except ValueError:
            print("This is not a number")
        else:
            # compare guess number to secret number
            if not guess_num == secret_num:
                if guess_num > secret_num:
                    print("Number is TOO HIGH")
                else:
                    print("Number is TOO LOW")
                attempts.append(guess_num)
            elif guess_num == secret_num:
                print("You got the number correct it was {} ".format(secret_num))
    else:
        again = input("Do you want to play again? y/n")
        if again == "y":
            game()
        else:
            print("Bye")

game()