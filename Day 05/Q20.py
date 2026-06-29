# Largest prime number
num = int(input("Enter number: "))
largest = 1

for i in range(2, num + 1):
    while num % i == 0:
        largest = i
        num //= i

print("Largest Prime Factor =", largest)