print("Enter three numbers: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest = num1
largest = num2

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num3 > largest:
    largest = num3
if num1 > largest:
    largest = num1

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")