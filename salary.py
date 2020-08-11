xa = input("Enter hours: ")
xb = input("Enter rate: ")
xc = float(xa)
xd = float(xb)
if xc>40 :
    xf = (xc-40)*(xd*0.5)
    xg = xc*xd
    xh = xf+xg
else:
    xh = xc*xd
print("Pay: ",xh)
 