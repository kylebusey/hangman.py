import random


class NumberGuesser():

    def guessNumber(number):
        number = int(random.randrange(0, 100))
        while True:
            guessedNumber = int(input("Please guess a number between 0 and 100.\n"))
            if guessedNumber > number:
                print("Your guess is too high.")
            elif guessedNumber < number:
                print("Your guess is too low.")
            else:
                print("You guessed correctly!")
                break

    guessNumber(number= 50)
