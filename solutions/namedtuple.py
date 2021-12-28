from collections import namedtuple

Car = namedtuple("Car", ["color", "make", "model", "mileage"])

my_car = Car("midnight silver", "Tesla", "Model Y", 5)

print(my_car)
