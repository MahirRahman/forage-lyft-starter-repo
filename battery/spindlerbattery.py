from abc import ABC
from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        # super.__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > 2:
            return True
        return False


