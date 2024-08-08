a=[1,4,5,7,9,0]
count=0
count1=0
for i in range(len(a)):
    if (a[i]%2==0):
        count+=1
    elif(a[i]%2==1):
        count1+=1
print("no. of odd numbers:",count1)
print("no. of even nos:",count)
