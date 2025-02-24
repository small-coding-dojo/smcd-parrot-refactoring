from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3

def parrot_factory(type_of_parrot, number_of_coconuts, voltage, nailed):
    match type_of_parrot:
        case ParrotType.EUROPEAN:
            return EuropeanParrot()
        case ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts)
        case ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(voltage, nailed)
        case _:
            return Parrot()


class Parrot:
    _BASE_SPEED = 12.0

    def speed(self):
        raise NotImplementedError("This parrot cannot move but it should")
            
    def cry(self):
        raise NotImplementedError("This parrot cannot cry but it should")


class EuropeanParrot  (Parrot) :
    # doesn't need any parameters at all
    def __init__(self):
        super().__init__()

    def cry(self):
        return "Sqoork!"
    
    def speed(self):
        return Parrot._BASE_SPEED


class AfricanParrot  (Parrot) :
    _BASE_LOAD_FACTOR = 9.0
    
    # needs only number of coconuts
    def __init__(self, number_of_coconuts):
        super().__init__()
        self._number_of_coconuts = number_of_coconuts

    def cry(self):
        return "Sqaark!"

    def speed(self):
        return max(0, Parrot._BASE_SPEED - AfricanParrot._BASE_LOAD_FACTOR * self._number_of_coconuts)



class NorwegianBlueParrot(Parrot):
    _MAXIMUM_VOLTAGE_SPEED = 24.0

    def __init__(self, voltage, nailed):
        super().__init__()
        self._voltage = voltage
        self._nailed = nailed

    def cry(self):
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."
        
    def speed(self):
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([self._MAXIMUM_VOLTAGE_SPEED, voltage * Parrot._BASE_SPEED])
