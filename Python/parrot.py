from enum import Enum




# todo: using enums can cause logic errors when the enum is extended and cases are forgotten in switch statements
class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3

def parrot_factory(type_of_parrot, number_of_coconuts, voltage, nailed):
    match type_of_parrot:
        case ParrotType.EUROPEAN:
            return EuropeanParrot(number_of_coconuts, voltage, nailed)
        case ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts, voltage, nailed)
        case ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(number_of_coconuts, voltage, nailed)
        case _:
            return Parrot(type_of_parrot, number_of_coconuts, voltage, nailed)

class Parrot:
    # todo: have a look where these variables are needed and pull them there
    base_speed = 12.0
    base_load_factor = 9.0


    # todo: type_of_parrot indicates that a sub-type should be present - the class may have multiple responsibilities
    # todo: we don't need all the parameters in constructor for all the parrots
    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed
        

    def speed(self):
        raise NotImplementedError("This parrot cannot move but it should")
            
    def cry(self):
        raise NotImplementedError("This parrot cannot cry but it should")


class EuropeanParrot  (Parrot) :
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)

    def cry(self):
        # todo: magic strings Sqoork, Sqaark,....
        return "Sqoork!"
    
    def speed(self):
        return Parrot.base_speed
    
class AfricanParrot  (Parrot) :
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)
        
    def cry(self):
        # todo: magic strings Sqoork, Sqaark,....
        return "Sqaark!"

    def speed(self):
        return max(0, Parrot.base_speed - self.base_load_factor * self._number_of_coconuts)



class NorwegianBlueParrot(Parrot):
    _maximum_voltage_speed = 24.0

    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)

    def cry(self):
        # todo: magic strings Sqoork, Sqaark,....
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."
        
    def speed(self):
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([self._maximum_voltage_speed, voltage * Parrot.base_speed])
