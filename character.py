#!/usr/bin/python3

from variance import create_variance
from numpy.random import choice, randint
import name_generator as ng
from traits import *


class Character(object):
    """Characters are the centerpiece of stories"""
    Name = Gender = Race = Appearance = Orientation = ''
    Traits = Story = []
    Age = 0

    def __init__(self,
                 cName,
                 cRace,
                 cGender,
                 cAge,
                 cAppearance,
                 cTraits,
                 cStory,
                 cOrientation=''):
        self.Name = cName
        self.Race = cRace
        self.Gender = cGender
        self.Age = cAge
        self.Appearance = cAppearance
        self.Traits = cTraits
        self.Story = cStory
        self.Orientation = cOrientation if cOrientation == '' else choice(
            ['Male', 'Female'])

    def from_dict(self, new_self):
        self.__dict__.update(new_self)

    def __str__(self):
        info = self.Name + """<div>""" + \
               """<ul><li><span style="font-weight:bold;">Race:</span> """ + self.Race + \
               """</li><li><span style="font-weight:bold;">Gender:</span> """ + self.Gender + \
               """</li><li><span style="font-weight:bold;">Age:</span> """ + str(self.Age) + \
               """</li><li><span style="font-weight:bold;">Appearance:</span> """ + str(self.Appearance) + \
               """</li><li><span style="font-weight:bold;">Trait 1:</span> """ + self.Traits[0] + "</li>"
        if len(self.Traits) > 1:
            info += """<li><span style="font-weight:bold;">Trait 2:</span> """ + self.Traits[
                1] + "</li>"
        info += "</ul><p>"
        for x in range(len(self.Story)):
            info += self.Story[x] + """</p>"""
            if x + 1 < len(self.Story):
                info += """<p>"""
        return info

    def from_dict(self, new_self):
        self.__dict__.update(new_self)


def create_person(pop):
    if pop is None:
        pop = create_variance()
    race = choice(list(pop.keys()), 1, p=list(pop.values()))[0]
    gender = choice(['Male', 'Female'], p=[0.5, 0.5])
    orientation = choice(
        ['Male', 'Female'],
        p=[0.042, 0.958] if gender == 'male' else [0.958, 0.042])
    name = ng.name_parser(race, gender)
    age = int(randint(ages[race][0], ages[race][1]))

    face = appearance['Face'][randint(len(appearance['Face']))]
    hair = appearance['Hair'][randint(len(appearance['Hair']))]
    eyes = appearance['Eyes'][randint(len(appearance['Eyes']))]
    body = appearance['Body'][randint(len(appearance['Body']))]
    appear = body + ' and looks ' + face.lower() + ' with ' + hair.lower(
    ) + ' hair and ' + eyes.lower() + ' eyes. '

    back = 'I\'m a ' + gender + ' ' + race + ', from '
    back += back_location[randint(len(back_location))] + ' who '
    back += back_story[randint(len(back_story))]

    trait = []
    demenor = randint(3)
    if demenor == 2:
        trait.append(positive_traits[randint(len(positive_traits))])
        trait.append(positive_traits[randint(len(positive_traits))])
    elif demenor == 1:
        trait.append(neutral_traits[randint(len(neutral_traits))])
        trait.append(neutral_traits[randint(len(neutral_traits))])
    else:
        trait.append(negative_traits[randint(len(negative_traits))])
        trait.append(negative_traits[randint(len(negative_traits))])

    story = [
        back,
    ]

    return Character(name, race, gender, age, appear, trait, story, orientation)
