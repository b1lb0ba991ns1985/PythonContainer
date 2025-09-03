car_makes = ('vw', 'bmw','fiat', 'nissan')

def format_object(makes):
    """
    :param makes: pre defined list of car manufacturers
    :return: formatted object with sorting
    """
    newCarsObject = []
    for car in makes:
        print(car)
        if car == 'vw' or car == 'bmw':
            newCarsObject.append(car.upper())
            continue
        else:
            newCarsObject.append(car.title())
            continue
    return sorted(newCarsObject)

formated_car_makes = format_object(car_makes)
print(formated_car_makes)