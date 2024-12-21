# Guess the number game.
import random
secret_number = random.randint(1,10)
print("I am thinking of a number between 1 and 10.")

for guess in range(1,6):
    print("Enter your guess: ")
    guessed_number = int(input())

    if guessed_number < secret_number:
        print("Your guess is too low.")
    elif guessed_number > secret_number:
        print("Your guess is too high.")
    else:
        break

if guessed_number == secret_number:
    print("Good Job!!! You guessed my number in " + str(guess) + " times")

else:
    print("Nope, The number i was thinking of was: " + str(secret_number))
    
