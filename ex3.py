'''
how_many = int(input("Please enter how many row you want to print:"))
how = int(input("1 or 0: "))
how = bool(how)
i = 1
while how ==True and i<=how_many:
    j = 1
    while j <= i:
        print("*",end = "")
        j +=1
    print()
    i +=1
while how == False and i<=how_many:
    j = 1
    while j <=how_many:
        print("*",end = "")
        j +=1
    print()
    how_many -=1 
    '''
how_many = int(input("Please enter how many row you want to print:"))
how = int(input("8 or 7: "))
how = bool(how)
if how == True:
    for i in range(1,how_many+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
elif how == False:
    for i in range(how_many,0,-1):
        for j in range(i,0,-1):
            print("*", end="")
        print()
        
        



    
    