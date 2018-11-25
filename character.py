#!/usr/bin/python3

from variance import create_variance
from numpy.random import choice, randint
import name_generator as ng
from traits import *


class Character(object):
    """Characters are the centerpiece of stories"""
    Name = Gender = Race = Appearance = ''
    Traits = Story = []
    Age = 0

    def __init__(self, cName, cRace, cGender, cAge, cAppearance, cTraits, cStory):
        self.Name = cName
        self.Race = cRace
        self.Gender = cGender
        self.Age = cAge
        self.Appearance = cAppearance
        self.Traits = cTraits
        self.Story = cStory

    def __str__(self):
        info = self.Name + """<div>""" + \
               """<ul><li><span style="font-weight:bold;">Race:</span> """ + self.Race + \
               """</li><li><span style="font-weight:bold;">Gender:</span> """ + self.Gender + \
               """</li><li><span style="font-weight:bold;">Age:</span> """ + str(self.Age) + \
               """</li><li><span style="font-weight:bold;">Appearance:</span> """ + str(self.Appearance) + \
               """</li><li><span style="font-weight:bold;">Trait 1:</span> """ + self.Traits[0] + "</li>"
        if len(self.Traits) > 1:
            info += """<li><span style="font-weight:bold;">Trait 2:</span> """ + self.Traits[1] + "</li>"
        info += "</ul><p>"
        for x in range(len(self.Story)):
            info += self.Story[x] + """</p>"""
            if x + 1 < len(self.Story):
                info += """<p>"""
        return info


def create_person(pop):
    if pop is None:
        pop = create_variance()
    race = choice(list(pop.keys()), 1, p=list(pop.values()))
    gender = choice(['Male', 'Female'])
    name = ng.name_parser(race, gender)
    age = randint(ages[race[0]][0], ages[race[0]][1])

    face = appearance['Face'][randint(len(appearance['Face']))]
    hair = appearance['Hair'][randint(len(appearance['Hair']))]
    eyes = appearance['Eyes'][randint(len(appearance['Eyes']))]
    body = appearance['Body'][randint(len(appearance['Body']))]
    appear = body + ' and looks ' + face.lower() + ' with ' + hair.lower() + ' hair and ' + eyes.lower() + ' eyes. '

    back = 'I\'m a ' + gender + ' ' + race[0] + ', from '
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

    story = [back, ]

    return Character(name, race[0], gender, age, appear, trait, story)
