import random
def computer():
    list1 = ["snake", "water", "gun"]
    c_choice = random.choice(list1)
    # print(c_choice)
    return c_choice
def win_loose():
    
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
    print(ai)
    print(pl)

# def how_wins():
#     if pl > ai:
#         print(f"You won!\n Your score" {pl} "Computer score" {ai})
#     elif pl < ai:
#         print("You Loose!\n Your score" {pl} "Computer score" {ai})
#     else:
#         print("Tied")

    
print("Welcome to snake water gun game!\n You have only 10 chances to win.")
chances =0

while chances<=9:
    ai = 0
    pl = 0
    player_input =input("Please enter your choice snake, water or gun: ")
    player_input = player_input.lower()
    win_loose()
    chances += 1
    print(f"You have {10-chances} left")
if chances >9:
    print("Game Over!")
    # how_wins()

