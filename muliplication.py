'''try:
    what_number = int(input("Which number multiplication do you need? "))
    how_much = int(input("How much multiplication do you need?"))
    for i in range(1,how_much+1):
        print(what_number,"*",i,"=",what_number*i)
except:
    print("Incorrect Input!")'''




try:
    what_number = int(input("Which number multiplication do you need? "))
    how_much = int(input("How much multiplication do you need?"))
    i = 1
    while i<=how_much:
        print(what_number,"*",i,"=",what_number*i)
        i +=1
except:
    print("Incorrect Input!")
