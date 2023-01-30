from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car

class CarFactory(Car):
    def Create_Calliope(self,current_date,last_service_date,current_mileage,last_service_mileage):
        Engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        Battery = SpindlerBattery(current_date,last_service_date)
        car = Car(Engine,Battery)
        return car
    def create_Glissade(self,current_date,last_service_date,current_mileage,last_service_mileage):
        Engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        Battery = SpindlerBattery(current_date,last_service_date)
        car = Car(Engine,Battery)
        return car
    def create_Palindrome(self,current_date,last_service_date,warning_light):
        Engine = SternmanEngine(last_service_date,warning_light)
        Battery = SpindlerBattery(current_date,last_service_date)
        car = Car(Engine,Battery)
        return car
    def create_Rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):
        Engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        Battery = NubbinBattery(current_date,last_service_date)
        car = Car(Engine,Battery)
        return car
    def create_Thovex(self,current_date,last_service_date,warning_light):
        Engine = CapuletEngine(last_service_date,warning_light)
        Battery = NubbinBattery(current_date,last_service_date)
        car = Car(Engine,Battery)
        return car