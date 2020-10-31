print("\n \t ~ Years Until 100 Demo ~ \n")
class charInt:
    def __init__(self, yearOfBirth):
        self.yearOfBirth = yearOfBirth
    
    def untilOneHund(yearOfBirth):
        current = 2020
        age = current - yearOfBirth
        yearsUntil100 = 100 - age
        return "You will turn 100 in " + str(yearsUntil100 + current)

yob = int(input("Enter your year of birth: "))
print(charInt.untilOneHund(yob))
