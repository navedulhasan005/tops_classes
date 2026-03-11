"""78)Write a python program to find the longest words."""

with open('demofile.txt', 'r') as file:
        text = file.read()
words = text.splitlines()
# long = max(words, key=len)
long = max(words)
print(long)
print(len(long))      