a=int(input("a:"))
b=int(input("b:"))
c=a and b
a=c or b
b=c or a
print("a:",b)
print("b:",a)
