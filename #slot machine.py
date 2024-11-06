#slot machine
import random, math

"""symbols = ['🍒',' 🍇', '🍉', '7️⃣',]
results = random.choices(symbols, k=3)
print(f'{results[0]} | {results[1]} | {results[2]}')
winning_symbol = '7️⃣'
if all(symbols == winning_symbol for symbol in symbols):
    print("Winner winner, Chicken Dinner")
else:
    print("Try again")"""

def Play():
    symbols = ['🍒',' 🍇', '🍉', '7️⃣',]
    winning_symbol = '7️⃣'

    while True:
        results = random.choices(symbols, k=3)
        print(f'{results[0]} | {results[1]} | {results[2]}')

        if all(symbols == winning_symbol for symbol in symbols):
            print("Winner winner, Chicken Dinner")
            break
        else:
            print("Try again")
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again != 'Y':
            print("Thanks for playing!")
            break
Play()