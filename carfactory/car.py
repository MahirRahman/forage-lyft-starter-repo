from engine.capuletengine import CapuletEngine
from engine.sternmanengine import SternmanEngine
from engine.willoughbyengine import WilloughbyEngine
from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery
from car import Car


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        c = Car(engine, battery)
        return c

    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        c = Car()
        c.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        c.battery = SpindlerBattery(current_date, last_service_date)
        return c

    def create_palindrome(current_date, last_service_date, warning_light_on: bool):
        c = Car()
        c.engine = SternmanEngine(warning_light_on)
        c.battery = SpindlerBattery(current_date, last_service_date)
        return c

    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        c = Car()
        c.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        c.battery = NubbinBattery(current_date, last_service_date)
        return c


    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        c = Car()
        c.engine = CapuletEngine(current_mileage, last_service_mileage)
        c.battery = NubbinBattery(current_date, last_service_date)
        return c