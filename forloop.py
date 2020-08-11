'''list1 = (["Apple", 1],["Banana",2], ["Orange",3])
dict1 = dict(list1)
print(dict1.values())

for fruit, quantity in dict1.items():
    print(fruit,quantity)'''
list2 = ["apple,", "banana", "cat",1,3,6,9,65,45,34]
for item in list2:
    if str(item).isnumeric() and item>6:
        print(item) 
