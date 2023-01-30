from tire.tires import Tires

from car import Car

class CarriganTires(Tires):
    def carrigan_tire(self,arr_produced):
        self.array_produced = arr_produced
    
    def needs_service(self):
        for value in self.array_produced:
            if value>=0.9:
                return True
        return False