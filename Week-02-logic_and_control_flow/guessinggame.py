import random
import time

print("------------------------------------------------------")
print("------hello welcome to the number guessing game------")
time.sleep(0.5)
print("------------------------------------------------------")
print("--------please select the level of dificullty--------")
print("------------------------------------------------------")
user_input = input("        ---easy--- ---medium--- ---Hard---")
print("------------------------------------------------------")



if user_input == "easy" or user_input == "Easy":
    print("you have 10 guesses to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(10):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
           print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries. You WIN!!!")
           break
        elif user_guess < random_number:
            print("your guess is too low")
        elif user_guess > random_number:
            print("your guess is too high")
        if i == 8:
            print(f"you have used all your guesses the number was {random_number} better luck next time")



elif user_input == "medium" or user_input == "Medium":
    print("you have 5 guesses to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(5):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
            print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries. You WIN!!!your good at this game")
            break
        elif user_guess < random_number:
            print("your guess is too low")
        elif user_guess > random_number:
            print("your guess is too high")
        if i == 4:
            print(f"you have used all your guesses the number was {random_number} better luck next time")



elif user_input == "Hard" or user_input == "hard":
    print("you have 3 guesses to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(3):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
            print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries. You WIN!!! your a pro at this game")
            break
        elif user_guess < random_number:
            print("your guess is too low")
        elif user_guess > random_number:
            print("your guess is too high")
        if i == 2:
            print(f"you have used all your guesses the number was {random_number} better luck next time")

else:
    print("invalid input please try again")
	


