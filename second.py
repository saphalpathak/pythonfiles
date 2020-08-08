try:
    s = input("Enter Value: ")
    r = float(s)
    if r < 10 :
        print("Smaller")
    elif r < 20 :
        print("Medium")
    else :
        print("Larger")
    print(" All Done")
except:
    print("Invalid input!")