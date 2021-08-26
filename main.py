height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
calculation = float(weight) / float(height) ** 2
bmi = int(calculation)
print(weight + " / " + height + " * " + height + " = " + str(calculation))
print(bmi)