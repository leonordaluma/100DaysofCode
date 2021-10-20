with open("file1.txt") as file1_numbers:
    file1_string = file1_numbers.readlines()
    file1_int = [int(num) for num in file1_string]

with open("file2.txt") as file2_numbers:
    file2_string = file2_numbers.readlines()
    file2_int = [int(num) for num in file2_string]

result = [num for num in file1_int if num in file2_int]
print(result)

