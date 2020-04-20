import random

value = random.randint(0,20)

userInput = input("Guess a number between 0 and 20: ")
integerUserInput = int(userInput)
print(value)


if(integerUserInput == value):
    print("You guessed correctly!")
elif(value - 5 < integerUserInput <= value + 5):
    print("You are close!")
if(integerUserInput > value ):
    print("Too High")
elif(integerUserInput < value - 5 < value):
    print("Too Low")
