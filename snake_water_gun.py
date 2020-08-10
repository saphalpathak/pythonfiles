import random
def computer():
    list1 = ["snake", "water", "gun"]
    c_choice = random.choice(list1)
    return c_choice
    # print(c_choice)
print("Welcome to snake water gun game!\n You have only 10 chances to win.")
chances = 0
while chances<=10:
    player_input = int(input("Please enter 1 for snake, 2 for water and 3 for gun: "))
    if computer() == "snake" and player_input == 1:
        print("Tied")
    elif computer() == "snake" and player_input == 2:
        print("You loose")
    elif computer() == "snake" and player_input == 3:
        print("You win")
    elif computer() == "water" and player_input == 1:
        print("You win")
    elif computer() == "water" and player_input == 2:
        print("Tied")
    elif computer() == "water" and player_input == 3:
        print("You loose")
    elif computer() == "gun" and player_input == 1:
        print("You loose")
    elif computer() == "gun" and player_input == 2:
        print("You won")
    elif computer() == "gun" and player_input == 3:
        print("Tied")
    chances +=1
    print("You have", (10-chances), "remaining")
    if chances >= 10:
        print("Game over!")
        break

