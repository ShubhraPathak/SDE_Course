# Build a Number guessing game, in which the user selects a range.
# --> A range input from user
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that
# integer in the minimum number of guesses
# --> randomly generated number from the program
# --> maximum number of attempt provided to user by the formula log2(B-A+1)
import math
import random


def guess_the_number():
    upper_limit = int(input("Please enter the upper limit :- "))
    lower_limit = int(input("Please enter the lower bound :- "))
    computer_guess = random.randint(lower_limit, upper_limit)
    total_attempts = round(math.log2(upper_limit-lower_limit+1))
    print("The maximum count in which you have to guess the randomly generated number is:",
          total_attempts)
    count = 0
    while count < total_attempts:
        count += 1
        print("This is your attempt:", count)
        user_guess = int(input("Guess the number:- "))
        if user_guess > computer_guess:
            print("try again you guessed too high!!")
        elif user_guess < computer_guess:
            print("try again you guessed too low!!")
        elif user_guess == computer_guess:
            print("Congratulations!!!!")
            break
    if count == total_attempts:
        print("You accedes the max try number, Better luck next time")


if __name__ == "__main__":
    guess_the_number()
