def harshad_number(num):
    num_str=str(num)
    digit_sum=sum(int(digit)for digit in num_str)
    return num%digit_sum==0
num=int(input("n:"))
if harshad_number(num):
    print("harshad number")
else:
    print("not a harshad number")
