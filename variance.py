#!/usr/bin/python3

import pickle
import numpy as np
from numpy.random import choice, randint
from tqdm import tqdm
import name_generator as ng
from traits import *

RACES = [
    'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Human', 'Half-Elf', 'Half-Orc',
    'Orc', 'Aasimer', 'Catfolk', 'Changeling', 'Dhampir', 'Drow', 'Duergar',
    'Fetchling', 'Gillman', 'Goblin', 'Grippli', 'Hobgoblin', 'Ifrit',
    'Kitsune', 'Kobold', 'Lizardfolk', 'Merfolk', 'Nagaji', 'Oread', 'Ratfolk',
    'Samsarans', 'Strix', 'Suli', 'Svirfneblin', 'Sylph', 'Tengu', 'Tiefling',
    'Undine', 'Vanara', 'Vishkanya', 'Wayangs'
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
    with open("settings.txt", 'r') as setting:
        s = setting.readlines()
        for x in range(len(s)):
            s[x] = s[x].rstrip('\n')

        # Check for Illegal Settings
        if s[0] not in RACES:
            print("Invalid Base Race")
            exit()
        if int(s[1]) <= 0:
            print("Invalid Population size")
            exit()
        if int(s[2]) < 0 or int(s[2]) > 100:
            print("Invalid Core Population Variance")
            exit()
        if int(s[3]) < 0 or int(s[3]) > 38:
            print("Invalid Exotic Race Count")
            exit()

        global settings
        settings = {
            'Race': s[0],
            'Population': int(s[1]),
            'Variance': int(s[2]),
            'Exotic': int(s[3]),
        }

    if settings is None:
        print("Unable to open settings")
        exit()


def custom_settings(ra, po, va, ex):
    global settings
    settings = {
        'Race': ra,
        'Population': po,
        'Variance': va,
        'Exotic': ex,
    }


def create_variance():
    global settings
    global global_pop
    if settings is None:
        load_settings()
    if global_pop is not None:
        return global_pop
    pop = {}
    if settings['Variance'] == 0:
        pop[settings['Race']] = 1.0
    else:  # Create Variance
        # Prime race
        base_pop = round(settings['Population'] / settings['Variance'])
        pop[settings['Race']] = base_pop

        # Add Exotics
        choices = choice(RACES, settings['Exotic'], replace=False)
        for i in choices:
            variance_degree = settings['Population'] - base_pop
            pop[i] = round(variance_degree / len(choices))

    global_pop = normalize_dict(pop)
    return global_pop


def create(l):
    v = np.array(l)
    if len(v.shape) < 2:
        print("Too little or irregular dimensions")
        exit()
    d = {}
    for x in v:
        d[x[0]] = int(x[1])
    return d


def from_file(file):
    with open(file, 'r') as f:
        content = f.readlines()
    l = []
    for line in content:
        l.append(line.split())
    return create(l)


def normalize_dict(v):
    d = {}
    total = sum(v.values())
    for x in v.keys():
        # print(x, v[x])
        d[x] = v[x] / total
    return d


def load(file):
    with open(file, 'rb') as f:
        v = pickle.load(f)
    return v


def save(variance, filename):
    with open(filename, 'wb') as f:
        pickle.dump(variance, f)


if __name__ == '__main__':
    rv = random_variance()
    test_var = normalize_dict(rv)
    custom_settings(BASE_RACES[randint(len(BASE_RACES))],\
        randint(1, 2147483647), randint(0, 100), randint(33))

    d = normalize_dict(test_var)
    save(d, 'test.pickle')
    print(load('test.pickle'))

    # from_file('test.txt')

    load_settings()
    draw = create_variance()
    # draw = custom.normalize_dict(custom.from_file('Sanos.txt'))

    population = list(draw.keys())
    density = [0] * len(population)

    for c in tqdm(range(settings['Population'])):
        pick = choice(list(draw.keys()), 1, p=list(draw.values()))
        for x in range(len(population)):
            if population[x] == pick:
                density[x] += 1

    print("End Results")
    for x in range(len(population)):
        print(population[x], '-', density[x])
