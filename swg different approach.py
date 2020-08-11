import random
def computer():
    list1 = ["snake", "water", "gun"]
    c_choice =random.choice(list1)
    return c_choice
def how_wins():
    if pl > ai:
        print(f"Congrats!!!!! You won!\nYour score {pl}\nComputer score {ai}")
    elif pl < ai:
        print(f"You Loose!\nYour score {pl}\nComputer score {ai}")
    else:
        print("Tied")
def win_loose():
    global ai
    global pl
    choice = computer()
    print(f"Computer choice: {choice}\nYour choice: {player_input}")
    if choice == "snake" and player_input == "snake":
        print("*****Tied*****")
    elif choice == "snake" and player_input == "water":
        print("*****You loose*****")
        ai += 1
    elif choice == "snake" and player_input == "gun":
        print("*****You win*****")
        pl += 1
    elif choice == "water" and player_input == "snake":
        print("*****You win*****")
        pl += 1
    elif choice == "water" and player_input == "water":
        print("*****Tied*****")
    elif choice == "water" and player_input == "gun":
        print("*****You loose*****")
        ai += 1
    elif choice == "gun" and player_input == "snake":
        print("*****You loose*****")
        ai += 1
    elif choice == "gun" and player_input == "water":
        print("*****You win*****")
        pl += 1
    elif choice == "gun" and player_input == "gun":
        print("*****Tied*****")
try:
    chances = 0
    ai = 0
    pl = 0
    while chances <=9:
        player_input =input("Please enter your choice snake, water or gun: ")
        player_input = player_input.lower()
        if (player_input != "gun" and player_input != "snake" and player_input != "water"):
            print("Invalid input   Choose between snake or water or gun")
            continue
        win_loose()
        chances +=1
        print(f"Your score: {pl}")
        print(f"Computer score: {ai}")
        print(f"You have {10-chances} chances left")
    if chances > 9:
            print("*******Game Over!*******")
            how_wins()
except:
    print("invalid input!")

