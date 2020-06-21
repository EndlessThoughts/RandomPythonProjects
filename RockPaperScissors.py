import random

randomGameOptions = random.randint(1, 3)
# print(randomGameOptions)

userInput = input("Rock[1], Paper[2] or Scissors[3]: ")
type_cast_user_input = int(userInput)

teamA = 0
teamB = 0

if type_cast_user_input == 0 or type_cast_user_input > 3:
    print("Number used is not valid")

if type_cast_user_input == randomGameOptions:
    print(userInput)
    print(randomGameOptions)
    print("We have a draw!")

elif type_cast_user_input == 1 and randomGameOptions == 3:
    print(userInput)
    print(randomGameOptions)
    teamA += 1
elif type_cast_user_input == 2 and randomGameOptions == 1:
    print(userInput)
    print(randomGameOptions)
    teamA += 1
elif type_cast_user_input == 3 and randomGameOptions == 2:
    print(userInput)
    print(randomGameOptions)
    teamA += 1
else:
    print("The user choice: " + str(userInput))
    print("The computer choice: " + str(randomGameOptions))
    teamB += 1

print("Team A Score: " + str(teamA))
print("Team B Score: " + str(teamB))
