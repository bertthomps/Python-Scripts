#!/usr/bin/env python

# Create a program to see if a number is divisible by another. If not divisable, the program will
# give the lowest divisible integer plus the remainder.

print('Welcome to the division app!')

x = int(input('First number? '))
y = int(input('Second number? '))

def main(x, y):
	z = x // y
	if x % y == 0:
		print('Cool, ' + str(x) + ' is divisable by '+ str(y) +' exactly ' + str(z) + ' times!')
	else:
		r = x % y
		print('Answer: ' + str(x) + ' is divisable by ' + str(y) + ' ' + str(z) + ' times. The remainder is ' + str(r) + '.')

main(x, y)