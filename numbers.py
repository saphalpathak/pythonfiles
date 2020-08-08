number = 7
r = 5
print("This is number gussing game and you only have 5 chances to win.")
print("Lets start!")
while True:
    input_number = int(input("Enter your number:"))
    if input_number > number:
        print("Sorry, Please enter lower number!")
    elif input_number == number:
        print("Congrats you won!")
        break

    else :
        print("Sorry, Please enter higher number!")
    r = r-1
    if 6>r>0:
        print("Your remaing moves is:",r)
        continue
    elif r == 0:
        print("Game Over!")
        break
    
    
    
    
    
    
    

    
