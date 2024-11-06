#Automate the boring stuff lesson 11
'''
def div42by(divideBy):
    try:
        return 42 /divideBy
    except ZeroDivisionError:
        print ("Error: You cannot divde by zero")

print (div42by(2))
print (div42by(12))
print (div42by(0))
print (div42by(24))
'''


print ("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("Holy shit you have a lot of fucking cats")
    else:
        print("Ha pussy thats not enough")
except ValueError:
    print("You did not enter a number you idiot")
