from resources import *
from numpy.random import randint, choice, random_sample
from character import create_person
from names import Antiques, Books, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons,\
    Jewelling, Brothel, Gunsmithing


SpellSource = json.load(open('settings.json', 'r'))['System']
if SpellSource == 'D&D 5':
    MasterSpells = json.load(open('5e_spells.json', 'r'), encoding='utf-8')
    MasterWondrous = json.load(open('5e_wondrous.json', 'r'), encoding='utf-8')
elif SpellSource == 'Pathfinder 1':
    MasterSpells = json.load(open('spells.json', 'r'), encoding='utf-8')
    MasterWondrous = json.load(open('wondrous.json', 'r'), encoding='utf-8')


def determine_cost(c):
    s = ""
    if isinstance(type(c), int):
        s = format(c, ',d') + " gp"
    else:
        if int(c) > 0:
            s += format(int(c), ',d') + " gp "
            c %= int(c)
        if int(c * 10) > 0:
            s += str(int(c * 10)) + " sp "
        if int((c * 100) % 10) > 0:
            s += str(int((c * 100) % 10)) + " cp"
    if len(s) == 0:
        s = "0 cp"
    return s


class Item:
    """Parent Class for All items"""
    Title: str = ""
    Description: str = ""
    Category: str = ""
    Link: str = ""
    Cost: float = 0
    Expandable: bool = False
    Linkable: bool = False

    def __str__(self):
        global MasterID
        s = '<tr><td style="width:50%;"><span class="text-md"'
        if self.Expandable:
            s += """onclick="show_hide('""" + str(MasterID) + """')" style="color:blue;"""
        s += '>'
        if self.Linkable:
            s += '<a href="' + self.Link + '">'
        s += self.Title
        if self.Linkable:
            s += '</a>'
        s += '</span>'
        if self.Description != "":
            s += '<br /><span class="text-sm emp"'
            if self.Expandable:
                s += ' id=\"' + str(MasterID) + '\" style="display: none;"'
                MasterID += 1
            s += '>' + self.Description + '</span>'
        s += '</td><td>' + determine_cost(self.Cost) + '</td><td>' + self.Category + '</td></tr>'
        return s


class Book(Item):
    g = {
        0: 'Children',
        1: 'Drama',
        2: 'Fiction',
        3: 'Horror',
        4: 'Humor',
        5: 'Mystery',
        6: 'Nonfiction',
        7: 'Romance',
        8: 'SciFi',
        9: 'Tome',
    }

    def __init__(self, rarity):
        self.Category = self.g[rarity]
        self.Title = str(Books(genre=self.Category))
        self.Cost = 0.5 + random_sample()


class Room(Item):
    def __init__(self, beds: int, qual: int):
        self.Title = str(beds) + " Beds"
        self.Cost = 0.5 * (qual + 1) * beds
        self.Description = ""
        self.Category = "Lodging"
        self.Link = ""
        self.Expandable = False
        self.Linkable = False
        # Necessary variable for replication
        self.Beds = beds


class Person(Item):
    Person = None

    def __init__(self, useless):
        # Even though this has an argument, It needs it, but it's useless
        self.Person = create_person(None)
        self.Title = self.Person.Name + ' (' + self.Person.Race + ')'
        self.Description = self.Person.Appearance + '; Age ' + str(self.Person.Age)
        self.Category = self.Person.Gender + ' wanting ' + self.Person.Orientation
        self.Cost = random_sample() + .1
        self.Expandable = False
        self.Linkable = False


class Food(Item):
    def __init__(self, rarity):
        s = ""
        meal_option = randint(15) + rarity
        if meal_option <= 10:
            self.Category = "Meat, Bread"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
        elif meal_option == 11:
            self.Category = "Meat, Bread, Fruit"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]

        elif meal_option == 12:
            self.Category = "Meat, Bread, Vegetable"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        elif meal_option == 13:
            self.Category = "Vegetable, Bread, Fruit"
            s += Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
        elif meal_option == 14:
            self.Category = "Meat, Fruit, Vegetable"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(len(Food_m3))]
            s += " with " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
            s += " and " + Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        else:
            self.Category = "Meat, Fruit, Vegetable, Bread"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " with " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
            s += " and " + Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        self.Title = s
        if meal_option == 0:
            self.Cost = (len(s) * random_sample() + .5) // 10
        else:
            self.Cost = (len(s) * sum(random_sample(meal_option))) // 10

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Title + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + self.Category + """</td></tr>"""
        return s


class Drink(Item):
    def __init__(self, level):
        s = ''
        num = randint(4) + level
        if num < 2:
            self.Category = "Non-Alcoholic"
            s += Drink_d1[randint(len(Drink_d1))]
        else:
            self.Category = "Alcoholic"
            s += Drink_d2[randint(len(Drink_d2))]
        self.Title = s
        if num == 0:
            self.Cost = (len(s) * random_sample() + .5) / 10
        else:
            self.Cost = (len(s) * sum(random_sample(num))) / 10

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Title + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + self.Category + """</td></tr>"""
        return s


class Jewel(Item):
    value = [
        10,
        50,
        100,
        500,
        1000,
        5000,
    ]
    Rarity = 0

    def __init__(self, rarity):
        self.Title = Jewelling.j1[randint(len(Jewelling.j1))] + Jewelling.j2[randint(len(Jewelling.j2))] + \
                     Jewelling.j3[randint(len(Jewelling.j3))]
        if rarity >= 5:
            rarity %= 5
        self.Rarity = rarity
        self.Cost = self.value[self.Rarity] * (random_sample() + 1)
        l = [
            'Low Quality Gems', 'Semi Precious Gems', 'Medium Quality Gemstones', 'High Quality Gemstones', 'Jewels',
            'Grand Jewels'
        ]
        self.Category = l[self.Rarity]


class Art(Item):
    materials = [['pewter', 'granite', 'soapstone', 'limestone', 'carved wood', 'ceramic'],
                 ['pewter', 'alabaster', 'silver', 'marble', 'bronze'],
                 ['pewter', 'alabaster', 'silver', 'marble', 'brass'], ['gold', 'adamantine', 'dragonbone', 'crystal']]
    gems = [[
        'n azurite', ' banded agate', ' blue quartz', ' hematite', ' lapis lazuli', ' malachite', ' moss agate',
        'n obsidian piece', ' tiger eye', ' beryl'
    ],
            [
                ' bloodstone', ' carnelian', ' chalcedony', ' citrine', ' jasper', ' moonstone', ' n onyx', ' zircon',
                ' chrysophase'
            ],
            [
                'n amber', 'n amethyst', ' piece of coral', ' garnet', ' piece of jade', ' pearl', ' spinel',
                ' tourmaline'
            ], ['n alexandrite', 'n aquamarine', ' topaz', ' peridot', ' blue spinel', ' black pearl', ' diamond']]
    filigree = [['copper', 'oak wood', 'tin', 'bronze', 'bone'], ['brass', 'maple wood', 'iron', 'glass', 'bone'],
                ['gold', 'mahogany wood', 'glass', 'ivory', 'mythril'], ['platinum', 'ironwood', 'mythril', 'ivory']]
    descriptor = [
        'ugly', 'beautiful', 'ancient', 'old', 'strange', 'antique', 'durable', 'sturdy', 'engraved', 'ornate', 'rough',
        'ornamental'
    ]
    cloth = ['silk', 'wool', 'leather', 'fur', 'angelskin', 'darkleaf', 'griffon mane']
    bad_condition = [
        'in poor condition', 'of poor craftsmanship', 'of shoddy construction', 'in bad shape', 'of low quality'
    ]
    figurine = [
        'a dragon', 'a gryphon', 'a hydra', 'an owlbear', 'a beholder', 'a boar', 'a bear', 'a wolf', 'a fox',
        'a tiger', 'a lion', 'a horse', 'an owl', 'a hawk', 'an eagle', 'a crow', 'a snake', 'a fish', 'a shark',
        'a goblin', 'a skeleton', 'an orc', 'a minotaur', 'a tiefling', 'a warrior', 'a knight', 'a thief', 'a wizard',
        'a ship', 'a castle', 'a tower', 'a boat', 'a king', 'a queen', 'a princess', 'a god', 'a goddess'
    ]
    object = [
        'ring', 'tankard', 'goblet', 'cup', 'drinking horn', 'crown', 'circlet', 'tiara', 'pendant', 'necklace',
        'amulet', 'medallion', 'bowl', 'plate', 'jewelry box', 'music box', 'brooch', 'chess set', 'mask', 'holy text',
        'hourglass', 'vase'
    ]
    magic = [
        'It glows with a soft blue light', 'It glows with a soft green light', 'It glows with a soft red light',
        'It glows with a soft amber light', 'It glows with a soft violet light', 'It is warm to the touch',
        'It is hot to the touch', 'It is cool to the touch', 'It is cold to the touch', 'It hums with gentle music',
        'It hums with melodic music', 'It hums with soft music', 'It is wreathed in blue flames',
        'It is wreathed in green flames', 'It is wreathed in red flames', 'It is wreathed in amber flames',
        'It is wreathed in violet flames'
    ]

    def __init__(self, quality):
        if quality > 5:
            quality %= 6
        c = randint(10)
        if quality == 0:
            c %= 3
            if c == 0:
                self.Description = choice(['Silvered', 'Gilded']) + ' ' + choice(['bottle', 'flask', 'jug']) + \
                                   ' of ' + choice(['dwarven', 'elven', 'Dragonborn']) + ' ' + \
                                   choice(['beer', 'wine', 'ale', 'mead'])
            elif c == 1:
                self.Description = 'Pair of ' + choice(self.descriptor) + ' ' + choice(self.cloth) + ' gloves'
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.cloth) + ' ' + choice(['hat', 'ribbon'])
        elif quality == 1:
            c %= 6
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', ' + choice(self.bad_condition)
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', ' + choice(self.bad_condition)
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[0])
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[0])
            elif c == 4:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[0])
            elif c == 5:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[0])
        elif quality == 2:
            c %= 2
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.cloth) + ' ' + \
                                   choice(['cloth', 'cloak']) + ' with ' + choice(self.materials[1]) + ' clasps'
            elif c == 1:
                self.Description = choice(self.descriptor) + ' belt with a(n) ' + choice(self.materials[1]) + ' buckle'
        elif quality == 3:
            c %= 8
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[2])
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[2])
            elif c == 4:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 5:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 6:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[2])
            elif c == 7:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[2])
        elif quality == 4:
            c %= 5
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[2])
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[2])
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[3])
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[3])
            elif c == 4:
                self.Description = choice(self.materials[3]) + ' framed painting of ' + choice(self.figurine)
        elif quality == 5:
            c %= 4
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[3]) + ' ' + \
                                   choice(self.magic)
        self.Description = self.Description.title()
        cost_factor = [50, 150, 500, 1000, 5000, 10000, 50000]
        self.Cost = cost_factor[quality + 1]
        self.Category = quality+1


class Wondrous(Item):
    Aura = Slot = ''
    CL = Weight = 0

    def __init__(self, cl=-1):
        self.Category = "Wondrous Item"
        self.Linkable = True
        if cl == -1 or SpellSource == 'D&D 5':
            pick = choice(list(MasterWondrous.keys()))
            self.Title = pick
            self.Link = MasterWondrous[pick]['Link']
            self.Cost = int(MasterWondrous[pick]['Price'])
            self.CL = MasterWondrous[pick]['CL']
            self.Aura = MasterWondrous[pick]['Aura']
            self.Slot = MasterWondrous[pick]['Slot']
            self.Weight = MasterWondrous[pick]['Weight']
        elif SpellSource == 'Pathfinder 1' and cl != -1:
            i = 0
            while True:
                pick = choice(list(MasterWondrous.keys()))
                if cl == int(MasterWondrous[pick]['CL']):
                    self.Title = pick
                    self.Link = MasterWondrous[pick]['Link']
                    self.Cost = int(MasterWondrous[pick]['Price'])
                    self.CL = int(MasterWondrous[pick]['CL'])
                    self.Aura = MasterWondrous[pick]['Aura']
                    self.Slot = MasterWondrous[pick]['Slot']
                    self.Weight = MasterWondrous[pick]['Weight']
                    break
                elif i == 100:
                    i = 0
                    cl = int(MasterWondrous[pick]['CL']) + 1
                else:
                    i += 1
        self.Description = 'Aura ' + self.Aura + '; CL ' + str(self.CL) + '; Weight ' + \
                           str(self.Weight) + '; Slot ' + self.Slot

