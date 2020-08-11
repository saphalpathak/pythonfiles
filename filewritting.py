# f = open("harry.txt","a")
# g = f.write("harry is good boy\n")
# print(g)
# f.close

# handle  read and write(r+)
f = open("harry.txt","r+")
g = f.read()
print(g)
f.write("thank you ")
f.write("so much")
f.close