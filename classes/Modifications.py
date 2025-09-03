from classes import car

class Modified(car.Car):

    def __init__(self, carMakeAndModel, carYear, carTransmission,
                 modifiedIntercooler = '', modifiedExhaust = '', modifiedIntake = '',
                 modifiedECU = ''):

        super().__init__(carMakeAndModel, carYear, carTransmission)
        self.modifiedIntercooler = modifiedIntercooler
        self.modifiedExhaust = modifiedExhaust
        self.modifiedIntake = modifiedIntake
        self.modifiedECU = modifiedECU

    def hasModifiedIntercooler(self, is_modified):
        """

        :param is_modified:
        :return:
        """
        if is_modified:
            self.modifiedIntercooler = 'Intercooler Upgraded'
        else:
            self.modifiedIntercooler = 'Not Modified'

    def hasModifiedExhaust(self, is_modified):
        if is_modified:
            self.modifiedExhaust = 'Exhaust Upgraded'
        else:
            self.modifiedExhaust = 'Not Modified'

    def hasModifiedIntake(self, is_modified):
        if is_modified:
            self.modifiedIntake = 'Intake Upgraded'
        else:
            self.modifiedIntake = 'Not Modified'

    def hasModifiedECU(self, is_modified):
        if is_modified:
            self.modifiedECU = 'ECU Upgraded'
        else:
            self.modifiedECU = 'Not Modified'

    def list_modifications(self):
        modified_parts = []
        stored_modifications = [self.modifiedIntercooler, self.modifiedExhaust, self.modifiedIntake, self.modifiedECU]

        for modification in stored_modifications:
            if not modification == 'Not Modified':
                modified_parts.append(modification)
                continue

        return modified_parts

