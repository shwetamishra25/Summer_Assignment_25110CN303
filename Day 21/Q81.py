#Program to find string length without using len()

text = input("Enter a string: ")

count = 0

for i in text:
    count = count + 1

print("Length of string =", count)