import sys
import random as rd

money = 100

#Coin Flip function
def coin_flip(guess, bet):
    #Flip assignment
    num = rd.randint(1, 2)
    if num == 1:
        flip = "Heads" #How to deal with upper / lower case guesses? heads/Heads?
    else:
        flip = "Tails"
    #Flip vs guess
    if guess == flip:
        print("You guess " + guess + " and the flip was " + flip + ". You won $" + str(bet) + ". Lucky guess!")
        return bet
    else:
        print("You guess " + guess + " and the flip was " + flip + ". You lost $" + str(bet) + ". Sucks to suck!")
        return -bet

#Cho-Han function
def cho_han(guess, bet):
    #Roll assignment
    roll1 = rd.randint(1, 6)
    roll2 = rd.randint(1, 6)
    if (roll1 + roll2) % 2 == 0:
        outcome = "Even"
    else:
        outcome = "Odd"
    #Roll vs guess
    if guess == outcome:
        print("You guess " + guess + " and the roll was " + outcome + ". You won $" + str(bet) + ". Good luck keeping this up!")
        return bet
    else:
        print("You guess " + guess + " and the roll was " + outcome + ". You lost $" + str(bet) + ". Two bad guesses in a row? Have you tried getting good?")
        return -bet

def cards(bet):
    #Cards assignment
    player1 = rd.randint(1,10) #How to actually draw a card from deck (weight probability for face cards)
    player2 = rd.randint(1,10) #How to subtract the player1 selection from player2 draw?
    #Winner determination
    if player1 > player2:
        print("You drew a " + str(player1) + " and your opponent drew a " + str(player2) + ". You drew the higher card and won $" + str(bet) + ". Don't get too cocky...")
        return bet
    elif player1 < player2:
        print("You drew a " + str(player1) + " and your opponent drew a " + str(player2) + ". You drew the lower card and lost $" + str(bet) + ". Today is just not your day...")
        return -bet
    else:
        print("You drew a " + str(player1) + " and your opponent drew a " + str(player2) + ". You drew the same card and didn't win or lose any money. What are the odds!")
        return 0

def bankrupt():
    if money <= 0:
        sys.exit("You lost it all and are now bankrupt. Better luck next year! \n")

def outcome():
    if money > 0:
        print("You now have $" + str(money) + ". \n")
    else:
        sys.exit("You lost it all and are now bankrupt. Better luck next year! \n")

#Call your game of chance functions here
print("Welcome to this year's addition of \"Let's Gamble Our Life Savings Away\"!")
print("You start with $" + str(money) + ". Let's gamble it away!" + "\n")

#Call Coin Flip Function
print("Game 1: Coin Flip!")
money += coin_flip("Heads", 45) #How to use user input? Terminal after commit? Web app? Through Flask?
bankrupt()
outcome()

#Call Cho Han Function
print("Game 2: Cho-Han!")
money += cho_han("Even", 50)
bankrupt()

#Call Card Function
print("Game 3: Card Picking!")
money += cards(373)
bankrupt()
