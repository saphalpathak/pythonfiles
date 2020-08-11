xa = input("Enter hours: ")
xb = input("Enter rate: ")

try:
    xc = float(xa)
    xd = float(xb)
except:
    print("Error, please enter numeric input")
    quit()
print(xc,xd)
# def main():
#     xh = xc*xd
if xc>40 :
    xf = (xc-40)*(xd*1.5)
    xg = xc*xd
    xh = xf+xg
else:
    main()
print("Pay: ",xh)
 
