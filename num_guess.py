print("******",  "GUSSING NUMBERS" , "******")

""" 
Generate a random number
Ask the user what number is on our mind(between 1 and 10)
Compare what the user enter to what we have generated 
if it is correct, say "You Win."
If it is not correct, say "Try Again"
"""
# Firstly, import the random modules

import random

def askForGuess():
    while True:
        guess = input('> ')  # Enter the guess.         
        
        if guess.isdecimal():
            return int(guess)  # Format to convert string guess to an integer.
            

# Generated a random number
random_num = random.randint(1, 10)
print("Let's Play the Gussing Numbers between 1 - 10")

# The user is only allowed to make 4 guesses
for x in range(4):
    print("Please enter a guess: ")
    guess = askForGuess()
    if guess == random_num:
        break

# Conditions
    if guess < random_num:
        print("Your number is high, TRY AGAIN !!!")
    elif guess > random_num:
        print("Your number is low, TRY AGAIN buddy !!!")

if guess == random_num:
    print()
    print("Cheers.... YOU WIN !!!")
else:
    print()
    print(f"You were close to getting it, so the actual number is {random_num}")    
    

print("Thanks for trying out this game, have a great day !!! ")


