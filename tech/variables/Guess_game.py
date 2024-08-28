import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game of sense!")
print("If you don't have sense don't play!!!")
print("Guess of a number between 1 and 100.")

while True:
            guess = int(input("Please!take a guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                     print("Please guess a number within the range of 1 to 100.")
            elif guess < number_to_guess:
                print("The number you guessed was too low! Try again.")
            elif guess > number_to_guess:
                print("The number you guessed was too high! Try again.")
            else:    
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

           