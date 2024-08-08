def count_words_lines(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_words, num_lines
text = input("Enter text: ")
words, lines = count_words_lines(text)
print("Number of words:", words)
print("Number of lines:", lines)
