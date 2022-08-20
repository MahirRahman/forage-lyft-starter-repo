from tires import Tires

class Carrigan(Tires):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for i in range(len(self.tire_wear)):
            if self.tire_wear[i] >= 0.9:
                return True
        return False


