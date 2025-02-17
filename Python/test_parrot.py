from parrot import Parrot, ParrotType, parrot_factory, AfricanParrot, EuropeanParrot, NorwegianBlueParrot


def test_speed_of_european_parrot():
    parrot = parrot_factory(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_cry_of_european_parrot():
    parrot = parrot_factory(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.cry() == "Sqoork!"


def test_speed_of_african_parrot_with_one_coconut():
    parrot = parrot_factory(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.speed() == 3.0


def test_cry_of_african_parrot():
    parrot = parrot_factory(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.cry() == "Sqaark!"

def test_cry_of_base_parrot():
    parrot = Parrot(ParrotType.AFRICAN, 1, 0, False)
    try:
        parrot.cry()
        assert False
    except NotImplementedError:
        pass


def test_speed_of_base_parrot():
    parrot = Parrot(ParrotType.AFRICAN, 1, 0, False)
    try:
        parrot.speed()
        assert False
    except NotImplementedError:
        pass    

def test_speed_of_african_parrot_with_two_coconuts():
    parrot = parrot_factory(ParrotType.AFRICAN, 2, 0, False)
    assert parrot.speed() == 0.0

def test_class_of_african_parrot():
    parrot = parrot_factory(ParrotType.AFRICAN, 2, 0, False)
    assert type(parrot) == AfricanParrot

def test_class_of_norwegian_blue_parrot():
    parrot = parrot_factory(ParrotType.NORWEGIAN_BLUE, 2, 0, False)
    assert type(parrot) == NorwegianBlueParrot

def test_class_of_european_parrot():
    parrot = parrot_factory(ParrotType.EUROPEAN, 2, 0, False)
    assert type(parrot) == EuropeanParrot

def test_speed_of_african_parrot_with_no_coconuts():
    parrot = parrot_factory(ParrotType.AFRICAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed():
    parrot = parrot_factory(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speed_norwegian_blue_parrot_not_nailed():
    parrot = parrot_factory(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage():
    parrot = parrot_factory(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.speed() == 24.0


def test_cry_norwegian_blue_parrot_high_voltage():
    parrot = parrot_factory(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.cry() == "Bzzzzzz"


def test_cry_norwegian_blue_parrot_no_voltage():
    parrot = parrot_factory(ParrotType.NORWEGIAN_BLUE, 0, 0, False)
    assert parrot.cry() == "..."

