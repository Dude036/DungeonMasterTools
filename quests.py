#!/usr/bin/python3

from beast_list import Beasts
from trinkets import Trinkets
from town_generator import create_person
from numpy.random import randint, choice
from traits import quest_location
from treasure import treasure_samples, Campaign_Speed


class QuestBoard(object):
    def __init__(self):
        pass


class Quest(object):
    Title = Hook = ''
    Reward = Level = 0
    Reporter = None

    def __init__(self, level):
        self.Level = int(level)
        # Create Person of interest and Reward
        self.Reporter = create_person(None)
        self.Reward = int(sum(treasure_samples(1, ['Coins'], Campaign_Speed[self.Level])))

        # Quest picker
        # r = randint(0, 5)
        r = randint(0, 2)
        if r == 0:
            self.__fetch()
        elif r == 1:
            self.__bounty()
        elif r == 2:
            self.__escort()
        elif r == 3:
            self.__escort()
        elif r == 4:
            self.__guild()

    def __fetch(self):
        # Retrieve stolen or rare item
        when = choice(['yesterday', 'the other day', 'a while ago', 'today', 'a fortnight ago', 'this week',
                       'this morning', 'last evening', 'last morning', 'a week ago', 'two days ago',
                       'three days ago', 'four days ago', 'five days ago', 'six days ago', 'recently',
                       'very recently', ])
        criminal = create_person(None)
        location = quest_location[randint(len(quest_location))]
        r = randint(0, 5)
        if r == 0:
            self.Title = 'Missing Item'
            item = choice(Trinkets)
            heritage = choice(['Brother', 'Sister', 'Mom', 'Dad', 'Parent', 'Sibling', 'Step-Brother', 'Step-Sister',
                               'Step-Mom', 'Step-Dad', 'Grandma', 'Grandpa', 'Uncle', 'Aunt', 'Great-Grandma',
                               'Great-Grandpa', 'Great-Uncle', 'Great-Aunt', ])

            self.Hook = "I seem to have lost something very close to me. It's \"" + item + '". My ' + heritage + \
                        ' gave it to me forever ago, and seem to have lost it. If you find it, please bring it to ' + \
                        self.Reporter.Name + ' ' + location + '.'
        if r == 1:
            self.Title = 'Stolen Item! HELP!'
            item = choice(Trinkets)

            self.Hook = 'A trinket of mine was rudely taken from me ' + when + '. I reported it to the police, but ' + \
                        'no effort to capture them has been made! I believe the crook to be ' + criminal.Name + ' (' + \
                        criminal.Gender + ' / ' + criminal.Race + ' / ' + str(criminal.Age) + ' years old)\nIf you ' + \
                        'apprehend them, see ' + self.Reporter.Name + ' ' + location + '. The trinket is "' + item + \
                        '".'
        elif r == 2:
            missing = create_person(None)
            self.Title = 'Missing Person: ' + missing.Name
            self.Hook = 'NOTICE: ' + missing.Name + ' has gone missing. They were last seen with ' + criminal.Name + \
                        '. If you have any information, please contact the authorities.\nRace: ' + missing.Race + \
                        '\nAge: ' + str(missing.Age) + '\nAppearance: ' + missing.Appearance
        elif r == 3:
            missing = create_person(None)
            self.Title = 'Kidnapped Person: ' + missing.Name
            self.Hook = 'NOTICE: ' + missing.Name + ' has been kidnapped. They were last seen with ' + criminal.Name + \
                        '( ' + criminal.Gender + ' / ' + criminal.Race + ' / ' + str(criminal.Age) + ' years old).' + \
                        ' If you have any information, please contact the authorities.\nRace: ' + missing.Race + \
                        '\nAge: ' + str(missing.Age) + '\nAppearance: ' + missing.Appearance
        elif r == 4:
            missing = create_person(None)
            time = str(randint(1, 13)) + ':' + choice(['00', '15', '30', '45'])
            self.Title = 'Search Party: ' + criminal.Name
            self.Hook = 'NOTICE: ' + missing.Name + ' has gone missing. ' + criminal.Name + ' has organized a ' + \
                        'searching party. If you have any information, report it to the authorities.\nIf you wish ' + \
                        'to join the search party, please see ' + criminal.Name + ' ' + location + '.'

    def __bounty(self):
        # Kill a monster or a criminal
        r = randint(0, 6)
        if r == 0:
            self.Title = 'Bounty: '
        elif r == 1:
            self.Title = 'Wanted: '
        elif r == 2:
            self.Title = 'Wanted (Dead of Alive): '
        elif r == 3:
            self.Title = 'Wanted (Dead: '
        elif r == 4:
            self.Title = 'Wanted (Alive): '
        elif r == 5:
            self.Title = 'Beware: '
        # Assassination target
        if randint(2) == 0:
            # Beast
            badCR = True
            while badCR:
                name = choice(list(Beasts.keys()))
                if int(float(Beasts[name]['CR'])) == self.Level:
                    badCR = False
            self.Title += name
            place = choice(['North', 'South', 'North-East', 'South-East', 'North-West', 'South-West', 'East', 'West'])
            self.Hook = 'A ' + name + ' has taken refuge ' + place + ' of town. They have cause great harm to us ' + \
                        'and we are looking for able bodies to help defeat this foe. If you are able, report to ' + \
                        self.Reporter.Name + ' for more information.\nReward: ' + str(self.Reward)
        else:
            # Criminal
            criminal = create_person(None)
            self.Title += criminal.Name
            self.Hook = criminal.Name + ' (' + criminal.Gender + ' / ' + criminal.Race + ' / ' + str(criminal.Age) + \
                        ' years old)\nAppearance: ' + criminal.Appearance + '\nIf you have any information, please ' \
                        'see ' + self.Reporter.Name + '\nReward: ' + str(self.Reward)

    def __escort(self):
        # Nobel seeking help through a shady place
        r = randint(0, 4)
        if r == 0:
            self.Title = 'Hired Hand Needed'
        elif r == 1:
            self.Title = 'Sellsword Wanted'
        elif r == 2:
            self.Title = 'Hired Hand Wanted'
        elif r == 3:
            self.Title = 'Sellsword Needed'
        elif r == 4:
            self.Title = 'Hiring Adventurers'

    def __guild(self):
        # All possible guild quests
        r = randint(0, 11)
        if r == 0:
            self.Title = 'Adventurers Guild: New Hires Wanted!'
        elif r == 1:
            self.Title = 'Arcane Guild: New Hires Wanted!'
        elif r == 2:
            self.Title = 'Laborers Guild: New Hires Wanted!'
        elif r == 3:
            self.Title = 'Performers Guild: New Hires Wanted!'
        elif r == 4:
            self.Title = 'Scholastic Guild: New Hires Wanted!'
        elif r == 5:
            self.Title = 'Merchant Guild: New Hires Wanted!'
        elif r == 6:
            self.Title = 'Bardic Guild: New Hires Wanted!'
        elif r == 7:
            self.Title = 'Military Guild: New Hires Wanted!'
        elif r == 8:
            self.Title = 'Thieves Guild: New Hires Wanted!'
        elif r == 9:
            self.Title = 'Assassin Guild: New Hires Wanted!'
        elif r == 10:
            self.Title = 'Gladiator Guild: New Hires Wanted!'

    def __str__(self):
        return ""


if __name__ == '__main__':
    print(Quest(0).Reward)
    print(Quest(1).Reward)
    print(Quest(2).Reward)
    print(Quest(3).Reward)
    print(Quest(4).Reward)
    print(Quest(5).Reward)
    print(Quest(6).Reward)
    print(Quest(7).Reward)
    print(Quest(8).Reward)
    print(Quest(9).Reward)
    print(Quest(10).Reward)
    print(Quest(11).Reward)
    print(Quest(12).Reward)
    print(Quest(13).Reward)
    print(Quest(14).Reward)
    print(Quest(15).Reward)
    print(Quest(16).Reward)
    print(Quest(17).Reward)
    print(Quest(18).Reward)
    print(Quest(19).Reward)
    print(Quest(20).Reward)
    print(Quest(21).Reward)
    print(Quest(22).Reward)
    print(Quest(23).Reward)
    print(Quest(24).Reward)
    print(Quest(25).Reward)
    print(Quest(26).Reward)
    print(Quest(27).Reward)
    print(Quest(28).Reward)
    print(Quest(29).Reward)
