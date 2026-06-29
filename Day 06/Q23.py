# Count set bits

num = int(input("Enter a number: "))

count = 0

while num > 0:
    count += num % 2
    num = num // 2

print("Set bits =", count)