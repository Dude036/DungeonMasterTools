from resources import MasterID, Food_f1, Food_m1, Food_v1, Food_g1, Food_f2, Food_m2, Food_v2, Food_g2, Food_m3,\
    Food_g3, Food_spice, Drink_d1, Drink_d2
from numpy.random import randint, choice, random_sample
from character import create_person
from names import Antiques, Books, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons,\
    Jewelling, Brothel, Gunsmithing


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
