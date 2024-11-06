#Zoltar fortune teller
import random
'''def fortune():
    random_fortune = random.randint(0,9)
    if random_fortune == 0:
        answer = "Fear the Old Blood"
    elif random_fortune == 1:
        answer = " The spirits are not pleased"
    elif random_fortune == 2:
        answer = "A corpse should be left well enough alone"
    elif random_fortune == 3:
        answer = "Kos, or as some say Kosem"
    elif random_fortune == 4:
        answer = "The ancient ones stir"
    elif random_fortune == 5:
        answer = "Wake from the dream"
    elif random_fortune == 6:
        answer = "Drums, drums in the deep"
    elif random_fortune  == 7:
        answer = "The darkness is coming"
    elif random_fortune  == 8:
        answer = "A hoonter must hoont"
    elif  random_fortune  == 9:
        answer = "They come"
    else:
        answer = "Time to Run"
    print(answer)
fortune()
fortune()
fortune()'''


options = ["Fear the Old Blood",
           "The spirits are not pleased",
           "A corpse should be left well enough alone",
           "Kos, or as some say Kosem",
           "The ancient ones stir",
           "Wake from the dream",
           "Drums, drums in the deep",
           "The darkness is coming",
           "A hoonter must hoont",
           "They come"
    ]
            
def  fortune():
    random_fortune = random.randint(0, len(options)-1)
    print(options[random_fortune])
fortune()
fortune()
fortune()
