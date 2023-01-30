from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self,current_date,last_service_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def engine_should_be_serviced(self):
        self.new_service_time = self.last_service_date.replace(self.last_service_date.year + 4)
        return self.new_service_time > self.current_date
