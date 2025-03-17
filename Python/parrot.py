from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __new__(cls, *args, **kwargs):
        # If the ctor is used by client code, then the object construction is hard to change
        # Wenn der ctor direkt verwendet wird, wird Client Code schwer zu ändern
        # Meta Programming in python is possible but hard to understand
        return super().__new__(AfricanParrot)

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        # This class has three reasons for change (single responsibility violated)
        # Some variables are only required by subtypes of a parrot
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed
        self._sub_parrot = self.get_sub_parrot()
 
    def speed(self):
         return self._sub_parrot.speed()

    def get_sub_parrot(self):
        # Switch case is duplicate - makes it hard to add more parrot types
        # Switch case executes specific logic for individual types of parrots
        # Implement and test default case
        match self._type:
            case ParrotType.EUROPEAN:
                sub_parrot = EuropeanParrot()
            case ParrotType.AFRICAN:
                sub_parrot = AfricanParrot(self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                sub_parrot = NorwegianParrot(self._voltage, self._nailed)
        return sub_parrot

    def cry(self):
         return self._sub_parrot.cry()

    # This method is only required for the NORWEGIAN_BLUE parrot
    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _base_speed(self):
        return 12.0
    

class EuropeanParrot (Parrot):
    def __init__(self):
        pass

    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot (Parrot):

    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def _load_factor(self):
        return 9.0

    def cry(self):
        return "Sqaark!"


class NorwegianParrot (Parrot):
    def __init__(self, voltage, nailed):
        self._nailed = nailed
        self._voltage = voltage

    def speed(self):
        # We dislike the single line if .. else .. construct
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."
