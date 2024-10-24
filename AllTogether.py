### Part Four -- your code goes here. 
#create list of 10 random numbers
import random
randomNumberList = []
for r in range(1,10):
    randomNumberList.append(random.randint(1,100))

index = 0
#check each number in the list
while index < len(randomNumberList):
    if (randomNumberList[index] % 2 == 0):
        #remove the even numbers
        randomNumberList.pop(index)
    else:
        #leave the odd numbers
        index = index+1

#display the remaining numbers
print(str(randomNumberList))