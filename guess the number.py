# exercise 3
# guess the number
import random

rand_num = random.randint(0,20)
guesses = 0
print("welcome to the game - Guess the number")
print("you have only 9 chances to guess the number\n")

while guesses < 9:
    inp = int(input("Enter a number: "))
    if inp > rand_num:
        print("\nenter a smaller number")
    elif 8-guesses == 0:
        print("\nYou didn't got the rand_numwer")
        # break
    elif inp < rand_num:
        print("\nEnter a Greater Number")
    else:
        print(f"\ncongratulation! you guessed the number it was {rand_num}")
        break

    print(8-guesses, "Guesses Left\n")
    guesses = guesses + 1