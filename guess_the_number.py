# Guess the number!
# importing the random module to generate random numbers
# guess is the variable to store the number I put in between 1 and 20
# exit to stop the loop from the number select section
# else and else if number matches == or < or > giving a different print
import random

number_to_guess = random.randint(1, 20)

for i in range(3):
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == number_to_guess:
        print("You got it! Well done for wasting your time.")
        break
    elif guess < number_to_guess:
        print("Hmm... Too Cold, Too Low.")
    else:
        print("Hmm... Too Hot, Too High")
else:
    print(f"Loser... you've ran out of guesses. The number was {number_to_guess}. You're a failure.")