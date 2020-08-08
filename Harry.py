print("You can search meaning of these words: Mutable, Immutable, Calculator, Fan")
word = input("Enter your word: ")
word = word.capitalize()
mydict = {"Mutable":"Changeable", "Immutable":"Not changeable", "Calculator":"Device where we can do mathematical calculation","Fan":"Device that gives air"}
#meaning = mydict[word]
print(mydict[word])
