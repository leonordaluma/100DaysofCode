height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
calculation = weight / height ** 2
bmi = int(calculation)
print(f"{weight} / {height} * {height} = {calculation}")
print(bmi)