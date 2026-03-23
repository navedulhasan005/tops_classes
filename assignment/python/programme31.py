"""31) Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given list 
of strings."""

list = ['abc', 'xyz', 'aba', '1221',"bbb"]
count = 0
for s in list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1
print(count)