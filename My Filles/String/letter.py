name = input("Enter name: ")
datee = input("Enter date: ")
letter = '''Dear name,
      You are selected!
      date: datee'''
letter = letter.replace("name",name)
letter = letter.replace("datee",datee)
print(letter)