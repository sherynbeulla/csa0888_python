a=[[1,2],[4,5]]
b=[[3,5],[6,4]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
        for i in range(len(c)):
            print(c)
