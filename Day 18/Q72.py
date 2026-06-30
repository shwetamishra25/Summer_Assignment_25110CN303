# Program to sort array in descending order

arr = list(map(int, input("Enter elements: ").split()))

arr.sort(reverse=True)

print("Descending Order:")
print(arr)