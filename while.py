while True:
    username = input("Enter your username: ")
    
    username = username.upper()
    # valid_username = "Saphal"
    # valid_username  =  "saphal"
    if (username == "Saphal"):
        print("Welcome", username)
        break
    elif (username != "Saphal"):
        print("Incorrect Username")
        
    