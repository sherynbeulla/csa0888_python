n = int(input("Enter a value: "))

if n > 1:
    c = int(n**0.5) + 1  
    for i in range(2, c):
        if n % i == 0:
            print("Prime number")
        else:
            print("Not a prime number")
