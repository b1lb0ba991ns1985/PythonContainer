from classes import Modifications
from classes import car

my_car = car.Car('BMW 420i', '2015', 'Manual')
my_modified_car = Modifications.Modified('BMW 420i', '2015', 'Manual')
my_modified_car.hasModifiedIntercooler(True)
my_modified_car.hasModifiedIntake(True)
my_modified_car.hasModifiedECU(True)
my_modified_car.hasModifiedExhaust(True)

for modification in my_modified_car.list_modifications():
    print(modification)
