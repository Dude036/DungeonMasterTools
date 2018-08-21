#!/usr/bin/python3

import pickle
import numpy as np
from numpy.random import choice, randint
from tqdm import tqdm
import name_generator as ng
from traits import *

BASE_RACES = ['Dwarf', 'Elf', 'Gnome', 'Halfling', 'Human', 'Half-Elf', 'Half-Orc', 'Orc']
EXOTIC = {
    'Aasimer' : 0.0237375,
    'Catfolk' : 0.03125,
    'Changeling' : 0.03125,
    'Dhampir' : 0.015625,
    'Drow' : 0.09375,
    'Duergar' : 0.015625,
    'Fetchling' : 0.015625,
    'Gillman' : 0.015325,
    'Goblin' : 0.11313125,
    'Grippli' : 0.015625,
    'Hobgoblin' : 0.11313125,
    'Ifrit' : 0.03125,
    'Kitsune' : 0.015625,
    'Kobold' : 0.09375,
    'Lizardfolk' : 0.015625,
    'Merfolk' : 0.0078125,
    'Nagaji' : 0.015625,
    'Oread' : 0.03125,
    'Ratfolk' : 0.09375,
    'Samsarans' : 0.015625,
    'Strix' : 0.015625,
    'Suli' : 0.015625,
    'Svirfneblin' : 0.015625,
    'Sylph' : 0.0237375,
    'Tengu' : 0.015625,
    'Tiefling' : 0.0625,
    'Undine' : 0.0078125,
    'Vanara' : 0.015625,
    'Vishkanya' : 0.0078125,
    'Wayangs' : 0.015625,
}

settings = None
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
        if s[0] not in BASE_RACES and s[0] not in list(EXOTIC.keys()):
            print("Invalid Base Race")
            exit()
        if int(s[1]) <= 0:
            print("Invalid Population size")
            exit()
        if int(s[2]) < 0 or int(s[2]) > 100:
            print("Invalid Core Population Variance")
            exit()
        if int(s[3]) < 0 or int(s[3]) > 32:
            print("Invalid Exotic Race Count")
            exit()
        
        global settings    
        settings = {
            'Race': s[0],
            'Population' : int(s[1]),
            'Variance' : int(s[2]),
            'Exotic' : int(s[3]),
        }
        
    if settings is None:
        print("Unable to open settings")
        exit()


def custom_settings(ra, po, va, ex):
    global settings
    settings = {
        'Race': ra,
        'Population' : po,
        'Variance' : va,
        'Exotic' : ex,
    }


def create_variance():
    global settings
    if settings is None:
        load_settings()
    pop = {}
    races = BASE_RACES
    if settings['Race'] in races:
        races.remove(settings['Race'])
    if settings['Variance'] == 0:
        pop[settings['Race']] = 1.0
    else: # Create Variance
        # Prime race
        pop[settings['Race']] = (100 - settings['Variance'])/100
        # Sub races
        for race in races:
            pop[race] = (settings['Variance'])/800
        
        # Add Exotics
        for _ in range(settings['Exotic']):
            r = [settings['Race']]
            while r[0] in pop:
                r = choice(list(EXOTIC.keys()), 1, list(EXOTIC.values()))
            pop[r[0]] = (settings['Variance']/800) * 1/settings['Exotic']

    return normalize_dict(pop)
    
 
def create(l):
    v = np.array(l)
    if len(v.shape) < 2:
        print("Too little or irregular dimensions")
        exit()
    d = {}
    for x in v:
        d[x[0]] = int(x[1])
    return d


def random_variance():
    var = {}
    for _ in range(randint(1, len(BASE_RACES) + len(EXOTIC))):
        choose = randint(2)
        if choose:
            var[BASE_RACES[randint(len(BASE_RACES))]] = randint(1, 101)
        else:
            var[list(EXOTIC.keys())[randint(len(EXOTIC))]] = randint(1, 101)
    return var
    
    
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
        d[x] = v[x]/total
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
    density = [0]*len(population)
    
    for c in tqdm(range(settings['Population'])):
        pick = choice(list(draw.keys()), 1, p=list(draw.values()))
        for x in range(len(population)):
            if population[x] == pick:
                density[x] += 1
    
    print("End Results")
    for x in range(len(population)):
        print(population[x], '-', density[x])
    
