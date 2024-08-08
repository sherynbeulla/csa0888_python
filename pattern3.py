def print_pattern(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, n + 1):
        print(alphabet[:i])
n = 5
print_pattern(n)
