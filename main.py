import random

playing = True

number = str(random.randint(10, 20))


while playing:
    num = input("Enter a number between 10 to 20:")

    if num == number:
        print("You've guessed it!!!!!!")

        break

    else:
        print("You didnt guess it right, go on............")