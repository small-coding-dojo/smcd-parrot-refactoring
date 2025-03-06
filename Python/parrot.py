from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        # This class has three reasons for change (single responsibility violated)
        # Some variables are only required by subtypes of a parrot
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        # Switch case is duplicate - makes it hard to add more parrot types
        # Switch case executes specific logic for individual types of parrots
        match self._type:
            case ParrotType.EUROPEAN:
                parrot = EuropeanParrot(self._type, self._number_of_coconuts, self._voltage, self._nailed)
                return parrot.speed()
            case ParrotType.AFRICAN:
                return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                # We dislike the single line if .. else .. construct
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        match self._type:
            case ParrotType.EUROPEAN:
                return "Sqoork!"
            case ParrotType.AFRICAN:
                return "Sqaark!"
            case ParrotType.NORWEGIAN_BLUE:
                # We dislike the single line if .. else .. construct
                return "Bzzzzzz" if self._voltage > 0 else "..."

    # This method is only required for the NORWEGIAN_BLUE parrot
    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    # This method is only required for the AFRICAN parrot
    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0
    

class EuropeanParrot (Parrot):
    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        super().__init__( type_of_parrot, number_of_coconuts, voltage, nailed)
    
    def speed(self):
        return self._base_speed()
    