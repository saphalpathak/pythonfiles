class Employee():
    no_of_leaves = 10
    pass
saphal = Employee()
rohan = Employee()
saphal.name = "saphal"
saphal.age = 27
saphal.position = "GM"
rohan.name = "rohan"  
rohan.age =  23
rohan.position = "Accountant"
 
Employee.no_of_leaves = 5
print(Employee.no_of_leaves)
print(rohan.no_of_leaves)
rohan.no_of_leaves = 8
print(rohan.no_of_leaves)

