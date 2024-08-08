def print_alphabet_pattern(n):
    current_char_code = ord('a')
    for i in range(1, n + 1):
        for j in range(i):
            if current_char_code > ord('z'):
                return
            print(chr(current_char_code), end="")
            current_char_code += 1
        print()
n = 5
print_alphabet_pattern(n)
