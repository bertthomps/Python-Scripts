#!/usr/bin/env python

# Number guessing game. The user inputs a number and the terminal says whether the actual number is higher or lower,
# until the user guesses correctly. At this point, the temrinal congradulates the user.

# Steps: 
# 1. Use python lib to generate random number (1-100)
# 2. If / then statements with print()s until user guesses correctly

import random

r = random.randint(1, 50)

def main():
	print('Welcome to Bert\'s guessing game! You\'ll never win!')
	while game() == False:
		game()
		if game() == True:
			break

def game():
	guess = input('What is your guess? ')
	if guess > r:
		print('Too high! Guess lower. ')
		return False
	elif guess < r:
		print('Too low! Guess higher. ')
		return False
	else:
		print('Congraduaions... I guess.')
		return True

main()
