#!/usr/bin/python3

from numpy.random import choice, randint
import simplejson as json

RACES = [
    # Pathfinder Races
    'Aasimer',
    'Catfolk',
    'Changeling',
    'Dhampir',
    'Drow',
    'Duergar',
    'Dwarf',
    'Elf',
    'Fetchling',
    'Gillman',
    'Gnome',
    'Goblin',
    'Grippli',
    'Half-Elf',
    'Half-Orc',
    'Halfling',
    'Hobgoblin',
    'Human',
    'Ifrit',
    'Kitsune',
    'Kobold',
    'Lizardfolk',
    'Merfolk',
    'Nagaji',
    'Orc',
    'Oread',
    'Ratfolk',
    'Samsarans',
    'Strix',
    'Suli',
    'Svirfneblin',
    'Sylph',
    'Tengu',
    'Tiefling',
    'Undine',
    'Vanara',
    'Vishkanya',
    'Wayangs',
    # D&D 5e races
    'Aarakocra',
    'Air Genasi',
    'Bugbear',
    'Centaur',
    'Dragonborn',
    'Earth Genasi',
    'Firbolg',
    'Fire Genasi',
    'Gith',
    'Goliath',
    # 'Grung', # Has yet to have a general name generator
    'Kalashtar',
    'Kenku',
    # 'Locathah',  # Has yet to have a general name generator
    'Loxodon',
    'Minotaur',
    'Shifter',
    'Simic Hybrid',
    'Tabaxi',
    'Tortle',
    'Triton',
    'Vedalken',
    'Warforged',
    'Water Genasi',
    'Yuan-ti Pureblood'
]

settings = None
global_pop = None


def load_settings():
    """ Settings
        1: Base population: see lists above
        2: Population Size: [1, Infinte)
        3: Core Population Variance: [0, 100] | 0 = No population Varience, 100 = Every Diverse
        4: Exotic Populations: [0, 32] | 0 = No exotic, 32 = All Exotic
    """
    global settings
    settings = json.loads(open('settings.json', 'r').read())

    if settings is None:  # Check for Illegal Settings
        print("Unable to open settings")
        exit()
    elif settings["Race"] not in RACES:
        print("Invalid Base Race")
        exit()
    elif settings["Population"] <= 0:
        print("Invalid Population size")
        exit()
    elif settings["Variance"] < 0 or settings["Variance"] > 100:
        print("Invalid Core Population Variance")
        exit()
    elif type(settings["Exotic"]) == type(0):
        if settings["Exotic"] < 0 or settings["Exotic"] > 62:
            print("Invalid Exotic Race Count")
            exit()


def custom_settings(ra, po, va, ex):
    global settings
    settings = {
        'Race': ra,
        'Population': po,
        'Variance': va,
        'Exotic': ex,
    }


def create_variance(predef={}):
    global settings
    global global_pop
    if predef != {}:
        settings = predef
    if settings is None:
        load_settings()
    if global_pop is not None:
        return global_pop
    pop = {}
    if settings['Variance'] == 0:
        pop[settings['Race']] = 1.0
    else:  # Create Variance
        # Prime race
        base_pop = settings['Population'] - round(settings['Population'] * (settings['Variance'] / 100))
        pop[settings['Race']] = base_pop

        # Add Exotics
        races = RACES
        races.remove(settings['Race'])
        if type(settings['Exotic']) == type([]):
            for i in settings['Exotic']:
                pop[i] = round(settings['Population'] * (settings['Variance'] / 100) / len(settings['Exotic']))
        else:
            choices = choice(races, settings['Exotic'], replace=False)
            for i in choices:
                pop[i] = round(settings['Population'] * (settings['Variance'] / 100) / settings['Exotic'])

    global_pop = normalize_dict(pop)
    return global_pop


def normalize_dict(v):
    d = {}
    total = sum(v.values())
    for x in v.keys():
        # print(x, v[x])
        d[x] = v[x] / total
    return d
