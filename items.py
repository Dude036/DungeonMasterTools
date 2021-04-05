from resources import MasterID
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
