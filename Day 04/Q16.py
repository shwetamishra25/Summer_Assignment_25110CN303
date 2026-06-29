# Armstrong number in range 
start = int(input("Start: "))
end = int(input("End: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    s = 0

    while temp > 0:
        digit = temp % 10
        s += digit ** digits
        temp //= 10

    if s == num:
        print(num, end=" ")