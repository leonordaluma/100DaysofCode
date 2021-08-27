import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, separated by a comma. ")
names = nameAsCSV.split(", ")
indices = len(names)
random_index = random.randint(0, indexes - 1)
print(f"{names[random_index]} is going to buy the meal today!")
# print(indexes)