class Employee():
    no_of_leaves = 10
    def __init__(self,aname,aage,aposition):
        self.name = aname
        self.age = aage
        self.position = aposition
    def printdetails(self):
        return f"Name is {self.name}, age is {self.age} and position is {self.position}"
    # @classmethod
    def change_no_of_leaves(clss,newleaves):
        clss.no_of_leaves = newleaves


saphal = Employee("saphal", 20 , "GM")
rohan = Employee("rohan", 19,"intern")
saphal.change_no_of_leaves(80)
print(Employee.no_of_leaves)

