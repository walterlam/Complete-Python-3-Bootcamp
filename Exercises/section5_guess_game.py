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

from random import randint
num = randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

trial = int(input('Type a number between 1 and 100\n'))
count = 1
prev = None 
while True:
    if trial < 1 or trial > 100:
        print('OUT OF BOUND')
        prev = trial
        trial = int(input('Type a number between 1 and 100\n'))
        count += 1
        continue
    
    if count == 1:
        if trial != num:
            if abs(trial - num) <= 10:
                print('WARM')
                prev = trial
                trial = int(input('Type a number between 1 and 100\n'))
                count += 1
            else:
                print('COLD')
                prev = trial
                trial = int(input('Type a number between 1 and 100\n'))
                count += 1
        else:
            print('CORRECT, finish in {} turns'.format(count))
            break
    else:
        if trial != num:
            if abs(trial - num) < abs(prev - num):
                print('WARMER')
                prev = trial
                trial = int(input('Type a number between 1 and 100\n'))
                count += 1
            else:
                print('COLDER')
                prev = trial
                trial = int(input('Type a number between 1 and 100\n'))
                count += 1
        else:
            print('CORRECT, finish in {} turns'.format(count))
            break

            
