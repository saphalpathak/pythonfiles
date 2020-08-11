import random
def computer():
    list1 = ["snake", "water", "gun"]
    c_choice = random.choice(list1)
    # print(c_choice)
    return c_choice
def win_loose():

    computer()
    if computer() == "snake" and player_input == 1:
        abc = "Tied"
        print(abc)
    elif computer() == "snake" and player_input == 2:
        abc = "You loose"
        print(abc)
        ai +=1
    elif computer() == "snake" and player_input == 3:
        abc = "You win"
        print(abc)
        pl += 1
    elif computer() == "water" and player_input == 1:
        abc = "You win"
        print(abc)
        pl += 1
    elif computer() == "water" and player_input == 2:
        abc = "Tied"
        print(abc)
    elif computer() == "water" and player_input == 3:
        abc = "You loose"
        ai += 1
        print(abc)
    elif computer() == "gun" and player_input == 1:
        abc = "You loose"
        ai += 1
        print(abc)
    elif computer() == "gun" and player_input == 2:
        abc = "You win"
        print(abc)
        pl += 1
    elif computer() == "gun" and player_input == 3:
        abc = "Tied"
        print(abc)

def how_wins():
    if pl > ai:
        print("You won!\n Your score", pl , "Computer score", ai)
    elif pl < ai:
        print("You Loose!\n Your score", pl , "Computer score", ai)
    else:
        print("Tied")

    
print("Welcome to snake water gun game!\n You have only 10 chances to win.")
chances = 0
while chances<=10:
    
    ai = 0
    pl = 0
    player_input = int(input("Please enter 1 for snake, 2 for water and 3 for gun: "))
    win_loose()
    chances +=1
    if chances >10:
        print("Game Over!")
        how_wins()
        break

