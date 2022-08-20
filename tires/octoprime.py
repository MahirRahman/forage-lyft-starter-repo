from tires import Tires

class Octoprime(Tires):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if sum(self.tire_wear) >= 3:
            return True
        return False


