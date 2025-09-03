class Car:
    """
        Simple clas to define a car
    """
    def __init__(self, carMakeAndModel, carYear, carTransmission):
        """
        :param carMakeAndModel:
        :param carYear:
        :param carTransmission:
        """

        self.carMakeAndModel = carMakeAndModel
        self.carYear = carYear
        self.carTransmission = carTransmission

    def drive(self):
        print(f"{self.carMakeAndModel} {self.carYear} {self.carTransmission} is now driving.")

    def stop(self):
        print(f"{self.carMakeAndModel} {self.carYear} {self.carTransmission} is STOPPED")

