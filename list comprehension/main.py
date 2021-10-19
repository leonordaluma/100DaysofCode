# name = "Leonor"
# print(name.upper())
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n * 2 for n in range(1,5)]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)