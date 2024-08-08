def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in input_string if char not in vowels])
    return result
user_input = input("Enter a string: ")
output_string = remove_vowels(user_input)
print("The string without vowels is:", output_string)
