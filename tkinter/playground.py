def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

# add(10,7,1,2)

def calculate(**kwargs):
    print(kwargs)

calculate(num1 = 1, num2 = 2)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Tesla")
print(my_car.make)
print(my_car.model)