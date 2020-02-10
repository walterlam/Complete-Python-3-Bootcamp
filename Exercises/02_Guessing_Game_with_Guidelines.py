# 02 Guessing Game with Guidelines

'''
Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players 
guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly
and how many guesses it took!
'''

'''
First, pick a random integer from 1 to 100 using the random module and assign
it to a variable
Note: random.randint(a,b) returns a random integer in range [a, b], 
including both end points.
'''

from random import randint
num = randint(1,100)

'''
Next, print an introduction to the game and explain the rules
'''

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


'''
Create a list to store guesses
Hint: zero is a good placeholder value. It's useful because it evaluates to "False"
'''
guesses = [0]

'''
Write a while loop that compares the player's guess to our number. 
If the player guesses correctly, break from the loop. 
Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
Some hints:

it may help to sketch out all possible combinations on paper first!
you can use the abs() function to find the positive difference between two numbers
if you append all new guesses to the list, then the previous guess is given as guesses[-2]
'''
while True:
    # everytime at the beginning of loop - guess again
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again:')
        continue
    
    if guess == num:
        print("CONGRATS, you found the number in {} rounds".format(len(guesses)))
        break
    else:
        guesses.append(guess)
        # when testing the first guess, guesses[-2]==0, which evaluates to False
        # and brings us down to the second section
        if guesses[-2]: # only 0 returns FALSE
            if abs(guess - num) < abs(guesses[-2] - num):
                print('WARMER')
            else:
                print('COLDER')
        else:
            if abs(guess-num) <= 10:
                print('WARM')
            else:
                print('COLD')
