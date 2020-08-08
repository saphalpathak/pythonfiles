def getdate():
    import datetime
    return datetime.datetime.now()
while True:
    try:
        query0 = int(input("Please enter 1 for log and 2 for retrive:  "))
        query1 = int(input("Please enter 1 for hari, 2 for ram and 3 for shyam : "))
        query2 = int (input("Please enter 1 for exercise and 2 for food : "))

        def exercise():
            if query1 == 1:
                if query2 == 1:
                    while True:
                        exercise_type = input("Please enter which type of exercise you have done: ")
                        with open("hari_ex.txt","a") as h:
                            h.write(str(getdate()) + " :  " + exercise_type +"\n")
                            print("Written successful!")
                            print("Do you want to enter exercise again?\n If yes press 1 otherwise press any numeric key: ")
                            query3 = int(input())
                            if query3 == 1:
                                continue
                            else:
                                break
            elif query1 == 2:
                if query2 == 1:
                    while True:
                        exercise_type = input("Please enter which type of exercise you have done: ")
                        with open("ram_ex.txt","a") as h:
                            h.write(str(getdate()) + " :  " + exercise_type + "\n")
                            print("Written successful!")
                            print("Do you want to enter exercise again?\n If yes press 1 otherwise press any numeric key: ")
                            query3 = int(input())
                            if query3 == 1:
                                continue
                            else:
                                break
            elif query1 == 3:
                if query2 == 1:
                    while True:
                        exercise_type = input("Please enter which type of exercise you have done: ")
                        with open("shyam_ex.txt","a") as h:
                            h.write(str(getdate()) + " :  " + exercise_type + "\n")
                            print("Written successful!")
                            print("Do you want to enter exercise again?\n If yes press 1 otherwise press any numeric key: ")
                            query3 = int(input())
                            if query3 == 1:
                                continue
                            else:
                                break
        def food():
            if query1 == 1:
                if query2 == 2:
                    while True:
                        food_type = input("Please enter which food do you eat: ")
                        with open("hari_food.txt","a") as h:
                            h.write(str(getdate()) + " :  " + food_type + "\n")
                            print("Written successful!")
                            print("Do you want to enter food again?\n If yes press 1 otherwise press any numeric key: ")
                            query3 = int(input())
                            if query3 == 1:
                                continue
                            else:
                                break
            elif query1 == 2:
                if query2 == 2:
                    while True:
                        food_type = input("Please enter which food do you eat:  ")
                        with open("ram_food.txt","a") as h:
                            h.write(str(getdate()) + " :  " + food_type + "\n")
                            print("Written successful!")
                            print("Do you want to enter food again?\n If yes press 1 otherwise press any numeric key: ")
                            query3 = int(input())
                            if query3 == 1:
                                continue
                            else:
                                break
            elif query1 == 3:
                if query2 == 2:
                    while True:
                        food_type = input("Please enter which food do you eat:  ")
                        with open("shyam_food.txt","a") as h:
                            h.write(str(getdate()) + " :  " + food_type + "\n")
                            print("Written successful!")
                            print("Do you want to enter food again?\n If yes press 1 otherwise press any numeric key: ")
                            query3 = int(input())
                            if query3 == 1:
                                continue
                            else:
                                break
        def retrive():
            if query1 == 1:
                if query2 == 1:
                    with open("hari_ex.txt") as h:
                        p = h.read()
                        print(p)
                elif query2 == 2:
                    with open("hari_food.txt") as h:
                        p = h.read()
                        print(p)
            elif query1 == 2:
                if query2 == 1:
                    with open("ram_ex.txt") as h:
                        p = h.read()
                        print(p)
                elif query2 == 2:
                    with open("ram_food.txt") as h:
                        p = h.read()
                        print(p)
            elif query1 == 3:
                if query2 == 1:
                    with open("shyam_ex.txt") as h:
                        p = h.read()
                        print(p)
                elif query2 == 2:
                    with open("shyam_food.txt") as h:
                        p = h.read()
                        print(p) 
        if query0 == 1:
            exercise()
            food()
        elif query0 == 2:
            retrive()
        print("Do you want to enter data again?\n If yes press 1 otherwise press any numeric key: ")
        query3 = int(input())
        if query3 == 1:
            continue
        else:
            print("Good Bye!")
            break

    except:
        print("Please enter valid input")
        continue

# This is test comment 2



