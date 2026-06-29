# Armstrong number
num = int(input("Enter number: "))
temp = num
digits = len(str(num))
s = 0

while num > 0:
    digit = num % 10
    s += digit ** digits
    num //= 10

if s == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong")