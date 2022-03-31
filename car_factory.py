from Batteries.battery import NubbinBattery, SplinderBattery
from Engines.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from car import Car

class CarFactory():

    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car


    def create_glissade(self,current_date,last_service_date,current_mileage,last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car


    def create_palindrome(self,current_date,last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car


    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car


    def create_thovex(self,current_date,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car                