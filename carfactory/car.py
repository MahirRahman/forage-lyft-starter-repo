from engine.capuletengine import CapuletEngine
from engine.sternmanengine import SternmanEngine
from engine.willoughbyengine import WilloughbyEngine
from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery
from car import Car


class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        c = Car(engine, battery)
        return c

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        c = Car(engine, battery)
        return c

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        c = Car(engine, battery)
        return c

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        c = Car(engine, battery)
        return c

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        c = Car(engine, battery)
        return c