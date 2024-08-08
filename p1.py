n=int(input(""))
a=-1
b=+1
c=a+b
for i in range(0,n+1):
    c=a+b
    a=b
    b=a
    print(i)
