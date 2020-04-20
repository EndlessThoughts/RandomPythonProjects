import random

value = random.randint(0,20)

def recurse():
 placeholder = True
 while(placeholder):
  userInput = input("Guess a number between 0 and 20: ")
  integerUserInput = int(userInput)
  if(integerUserInput == value):
    print("You guessed correctly!")
    break
  elif(value - 5 < integerUserInput <= value + 3):
    print("You are close!")
  elif(integerUserInput > value ):
    print("Too High")
  elif(integerUserInput < value - 5 < value):
    print("Too Low")
  else:
    recurse()
    break
recurse()
