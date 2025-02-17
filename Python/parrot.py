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

    # todo: type_of_parrot indicates that a sub-type should be present - the class may have multiple responsibilities
    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed
        


    def speed(self):
        # todo: repeated switches smell - replace conditional w/ polymorphism
        match self._type:
            case ParrotType.EUROPEAN:
                return self._base_speed()
            case ParrotType.AFRICAN:
                return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        # todo: repeated switches smell - replace conditional w/ polymorphism
        match self._type:
            case ParrotType.NORWEGIAN_BLUE:
                # todo: if 0 is modified to 1 no test breaks (atleast 1 test case is missing)
                return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage):
        # todo: magic number 24
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        # todo: magic number 9
        return 9.0

    def _base_speed(self):
        # todo: magic number 12
        return 12.0

class EuropeanParrot  (Parrot) :
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)

    def cry(self):
        # todo: magic strings Sqoork, Sqaark,....
        return "Sqoork!"
    
class AfricanParrot  (Parrot) :
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)
        
    def cry(self):
        # todo: magic strings Sqoork, Sqaark,....
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)

    def cry(self):
        # todo: magic strings Sqoork, Sqaark,....
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."