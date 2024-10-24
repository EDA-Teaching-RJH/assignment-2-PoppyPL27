### Part Two -- your code goes here. 
import random

randomNumber = random.randint(1,100)
guess = 0;

while (randomNumber != guess):
    guess = int(input("the number is in between 1 and 100. guess what the number is: "))

print("you guessed correctly! the number was "+str(randomNumber))