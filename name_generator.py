from numpy.random import randint
from names import *

d_name = [
    'Aasimer',
    'Centaur',
    'Dragonborn',
    'Drow',
    'Duergar',
    'Dwarf',
    'Elf',
    'Goblin',
    'Goliath',
    'Human',
    'Half-Orc',
    'Half-Elf',
    'Merfolk',
    'Orc',
    'Simic Hybrid',
    'Svirfneblin',
    'Tian',
    'Tengu',
    'Tiefling',
    'Triton',
]
d_single = [
    'Catfolk',
    'Firbolg',
    'Fetchling',
    'Gith',
    'Gnome',
    'Halfling',
    'Hobgoblin',
    'Ifrit',
    'Kalashtar',
    'Kitsune',
    'Kobold',
    'Lizardfolk',
    'Loxodon',
    'Minotaur',
    'Nagaji',
    'Oread',
    'Ratfolk',
    'Samsarans',
    'Sylph',
    'Undine',
    'Vedalken',
]
d_premade = [
    'Dhampir',
    'Gillman',
    'Grippli',
    'Shifter',
    'Strix',
    'Vishkanya',
    'Wayangs',
]
d_unisex = [
    'Aarakocra', 'Bugbear', 'Changeling', 'Kenku', 'Tabaxi', 'Tortle',
    'Warforged', 'Yuan-ti Pureblood'
]


def default_name(race, gender='Male', doubled=True):
    """ Races under this category
    Aasimer, Drow, Duergar, Dwarf, Elf, Goblin, Human, Half-Orc, Half-Elf, Orc, Svirfneblin, Tian, Tengu, Tiefling
    """
    # First name
    name = ''
    if gender == 'Male':
        name += race.m1[randint(len(race.m1))] + race.m2[randint(len(
            race.m2))] + race.m3[randint(len(race.m3))]
        if randint(2) == 1 and doubled:
            name += race.m2[randint(len(race.m2))] + race.m3[randint(
                len(race.m3))]
        name += race.m4[randint(len(race.m4))]

    else:  # Female
        name += race.f1[randint(len(race.f1))] + race.f2[randint(len(
            race.f2))] + race.f3[randint(len(race.f3))]
        if randint(2) == 1 and doubled:
            name += race.f2[randint(len(race.f2))] + race.f3[randint(
                len(race.f3))]
        name += race.f4[randint(len(race.f4))]

    # Last name
    name += ' ' + race.s1[randint(len(race.s1))] + race.s2[randint(
        len(race.s2))] + race.s3[randint(len(race.s3))]
    if randint(2) == 1 and doubled:
        name += race.s2[randint(len(race.s2))] + race.s3[randint(len(race.s3))]
    name += race.s4[randint(len(race.s4))]

    return name.title()


def default_single(race, gender='Male', doubled=True):
    """ Races under this category
    Catfolk, Fetchling, Gnome, Halfling, Hobgoblin, Ifrit, Kobold, Kitsune, Lizardfold, Nagaji, Oread, Ratfolk, Samsarans, Sylph, Undine, Vishkanya
    """
    name = ''
    if gender == 'Male':
        name += race.m1[randint(len(race.m1))] + race.m2[randint(len(
            race.m2))] + race.m3[randint(len(race.m3))]
        name += race.m2[randint(len(race.m2))] + race.m4[randint(len(race.m4))]
        if randint(2) == 1 and doubled:
            name += race.m3[randint(len(race.m3))] + race.m2[randint(
                len(race.m2))] + race.m4[randint(len(race.m4))]

    else:  # Female
        name += race.f1[randint(len(race.f1))] + race.f2[randint(len(
            race.f2))] + race.f3[randint(len(race.f3))]
        name += race.f2[randint(len(race.f2))] + race.f4[randint(len(race.f4))]
        if randint(2) == 1 and doubled:
            name += race.f2[randint(len(race.f2))] + race.f3[randint(
                len(race.f3))] + race.f4[randint(len(race.f4))]

    return name.title()


def default_premade(race, gender='Male', single=False):
    """ Races under this category
    Dhampir, Gillman, Grippli, Merfolk, Strix, Wayangs
    """
    name = ''
    if gender == 'Male':
        name += race.m1[randint(len(race.m1))]
    else:
        name += race.f1[randint(len(race.f1))]
    if not single:
        name += ' ' + race.s1[randint(len(race.s1))]
    return name.title()


def default_unisex(race, quantity=5):
    s = race.n1[randint(len(race.n1))]
    if quantity >= 2:
        s += race.n2[randint(len(race.n2))]
    if quantity >= 3:
        s += race.n3[randint(len(race.n3))]
    if quantity >= 4:
        s += race.n4[randint(len(race.n4))]
    if quantity >= 5:
        s += race.n5[randint(len(race.n5))]
    return s.title()


def vanara(gender='Male'):
    s = Vanara.n1[randint(len(Vanara.n1))]
    if gender == 'Male':
        s += Vanara.n2[randint(len(Vanara.n2))]
    else:
        s += Vanara.n3[randint(len(Vanara.n3))]
    return s.title()


def genasi(race):
    if 'Air' in race:
        return Genasi.a1[randint(len(Genasi.a1))]
    elif 'Earth' in race:
        return Genasi.e1[randint(len(Genasi.e1))]
    elif 'Fire' in race:
        return Genasi.f1[randint(len(Genasi.f1))]
    elif 'Water' in race:
        return Genasi.w1[randint(len(Genasi.w1))]


def suli(gender='Male'):
    s = default_name(Suli, gender) + ' the ' + Suli.t1[randint(len(Suli.t1))]
    return s.title()


def name_parser(race, gender):
    name = ''
    if race in d_name:
        if race == 'Aasimer':
            name = default_name(Aasimer, gender)
        elif race == 'Centaur':
            name = default_name(Aasimer, gender)
        elif name == 'Dragonborn':
            name = default_name(Dragonborn, gender)
        elif race == 'Drow':
            name = default_name(Drow, gender)
        elif race == 'Duergar':
            name = default_name(Duergar, gender, False)
        elif race == 'Dwarf':
            name = default_name(Dwarf, gender)
        elif race == 'Elf':
            name = default_name(Elf, gender)
        elif race == 'Goblin':
            name = default_name(Goblin, gender, False)
        elif race == 'Goliath':
            name = default_name(Goliath, gender, False)
        elif race == 'Human':
            name = str(Human(gender))
        elif race == 'Half-Elf':
            name = default_name(HalfElf, gender)
        elif race == 'Half-Orc':
            name = default_name(HalfOrc, gender)
        elif race == 'Merfolk':
            name = default_name(Merfolk, gender)
        elif race == 'Orc':
            name = default_name(Orc, gender)
        elif race == 'Svirfneblin':
            name = default_name(Svirfneblin, gender)
        elif race == 'Tian':
            name = default_name(Tian, gender)
        elif race == 'Tengu':
            name = default_name(Tengu, gender)
        elif race == 'Tiefling':
            name = default_name(Tiefling, gender)
        elif race == 'Triton':
            name = default_name(Triton, gender) + 'ath'

    elif race in d_single:
        if race == 'Catfolk':
            name = default_single(Catfolk, gender)
        elif race == 'Firbolg':
            name = default_single(Firbolg, gender, False)
        elif race == 'Fetchling':
            name = default_single(Fetchling, gender)
        elif race == 'Gith':
            name = default_single(Gith, gender, False)
        elif race == 'Gnome':
            name = default_single(Gnome, gender)
        elif race == 'Halfling':
            name = default_single(Halfling, gender)
        elif race == 'Hobgoblin':
            name = default_single(Hobgoblin, gender)
        elif race == 'Ifrit':
            name = default_single(Ifrit, gender)
        elif race == 'Kalashtar':
            name = default_single(Kalashtar, gender)
        elif race == 'Kitsune':
            name = default_single(Kitsune, gender)
        elif race == 'Kobold':
            name = default_single(Kobold, gender)
        elif race == 'Lizardfolk':
            name = default_single(Lizardfolk, gender)
        elif race == 'Loxodon':
            name = default_single(Loxodon, gender)
        elif race == 'Minotaur':
            name = default_single(Minotaur, gender)
        elif race == 'Nagaji':
            name = default_single(Nagaji, gender)
        elif race == 'Oread':
            name = default_single(Oread, gender)
        elif race == 'Ratfolk':
            name = default_single(Ratfolk, gender)
        elif race == 'Samsarans':
            name = default_single(Samsarans)
        elif race == 'Simic Hybrid':
            name = str(SimicHybrid(gender))
        elif race == 'Sylph':
            name = default_single(Sylph, gender)
        elif race == 'Undine':
            name = default_single(Undine, gender)
        elif race == 'Vedalken':
            name = default_single(Vedalken, gender)

    elif race in d_premade:
        if race == 'Dhampir':
            name = default_premade(Dhampir, gender)
        elif race == 'Gillman':
            name = default_premade(Gillman, gender, True)
        elif race == 'Grippli':
            name = default_premade(Grippli, gender, True)
        elif race == 'Shifter':
            name = default_premade(Shifter, gender, True)
        elif race == 'Strix':
            name = default_premade(Strix, gender)
        elif race == 'Vishkanya':
            name = default_premade(Vishkanya, gender)
        elif race == 'Wayangs':
            name = default_premade(Wayangs, gender, True)

    elif race in d_unisex:
        if race == 'Aarakocra':
            name = default_unisex(Aarakocra, 5)
        elif race == 'Changeling':
            name = default_unisex(Changeling, 4)
        elif race == 'Bugbear':
            name = default_unisex(Bugbear, 5)
        elif race == 'Kenku':
            name = default_unisex(Kenku, 1)
        elif race == 'Tabaxi':
            name = default_unisex(Tabaxi, 1)
        elif race == 'Tortle':
            name = default_unisex(Tortle, 4)
        elif race == 'Warforged':
            name = default_unisex(Warforged, 1)
        elif race == 'Yuan-ti Pureblood':
            name = default_unisex(Yuanti, 4)

    elif race == 'Vanara':
        name = vanara(gender)
    elif race == 'Suli':
        name = suli(gender)
    elif 'Genasi' in race:
        name = genasi(race)
    else:
        name = None
    return name
