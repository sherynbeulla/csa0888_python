a = int(input("decimal number:"))
binary_num = ""
n = a
if n == 0:
    binary_num = "0"
else:
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
print("Output:", binary_num)

