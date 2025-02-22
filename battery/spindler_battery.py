from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        # super.__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > 3:
            return True
        return False


