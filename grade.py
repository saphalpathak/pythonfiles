score = input("Enter numeric value: ")
 try:
     score  = float(score)
     if score > 1.0:
         print("Bad number")
     elif 1.0 >= score>=0.9:
         print("A")
     elif .9>=score>=.8:
         print("B")
     elif 0.8>=score>=0.7:
         print("C")
     elif .7>=score>=.6:
         print("D")
     elif .6>=score>=0.5:
         print("F")
 except:
     print("Please enter numeric value")
             