from tire.tires import Tires

from car import Car

class OctoprimeTire(Tires):
    def octoprime_tire(self,array_produced):
        self.array_produced = array_produced

    def needs_service(self):
        if sum(self.array_produced) >= 3:
            return True
        return False