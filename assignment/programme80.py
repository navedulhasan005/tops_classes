"""80)Write a Python program to count the frequency of words in a file."""

with open('demofile.txt', 'r') as file:
    text = file.read()
    word = text.split()
    word_count = {}
    for i in word:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
print(word_count)
