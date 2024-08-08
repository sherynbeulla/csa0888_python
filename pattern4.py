def print_pattern(n):
    for i in range(1, n + 1):
                char = chr(96 + i)
                print(char * i)
n = 5  
print_pattern(n)
