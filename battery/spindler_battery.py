from abc import ABC
from utils import add_years_to_date
from car import Car

class SpindlerBattery(Car,ABC):
    def __init__(self,current_date,last_service_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def engine_should_be_serviced(self):
        self.new_service_time = add_years_to_date(self.last_service_date,2)
        return self.new_service_time > self.current_date
