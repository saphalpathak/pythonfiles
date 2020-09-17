# Program
def format_name(first_name,last_name):
    if (first_name != "" and last_name !=""):
        string = "Name:" + last_name + "," + first_name
        return string
    elif (first_name !="" or last_name !=""):
        string = "Name:" + first_name + last_name
        return string
    else:
        string = ""
        return string
    
print(format_name("Saphal","Pathak"))
print(format_name("","Pathak"))
print(format_name("Saphal",""))
print(format_name("",""))
