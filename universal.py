 # recursion
# n= int(input())
# def function(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return (n-1) + (n-2)
# print(function(n))
# comment
# This is comments
b = 0
c = 0
def what():
    a = 0
    while a <10:
        d = int(input())
        e = int(input())
        if d > e:
            print(f"you won")
            global b
            b +=1
        else:
            print(f"you loose")
            global c 
            c +=1
        a +=1
what()
print(b)
print(c)
