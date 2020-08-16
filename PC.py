#!/usr/bin/python3

from numpy.random import randint, choice
from character import Character, create_person
from resources import MasterSpellBlacklist
from stores import Weapon
import simplejson as json
import re

MasterSpells = json.load(open('spells.json', 'r'), encoding='utf-8')

# A list of what stats are import to what character.
# This is somewhat just an opinion, so if you feel it's different, then change it.
playable = {
    "Barbarian": {
        "STR": 0,
        "DEX": 1,
        "CON": 2,
        "INT": 4,
        "WIS": 3,
        "CHA": 5
    },
    "Bard": {
        "STR": 5,
        "DEX": 1,
        "CON": 2,
        "INT": 3,
        "WIS": 4,
        "CHA": 0
    },
    "Cleric": {
        "STR": 2,
        "DEX": 4,
        "CON": 1,
        "INT": 5,
        "WIS": 0,
        "CHA": 3
    },
    "Druid": {
        "STR": 3,
        "DEX": 1,
        "CON": 2,
        "INT": 4,
        "WIS": 0,
        "CHA": 5
    },
    "Fighter": {
        "STR": 0,
        "DEX": 1,
        "CON": 2,
        "INT": 4,
        "WIS": 3,
        "CHA": 5
    },
    # "Magus": {
    #     "STR": 3,
    #     "DEX": 0,
    #     "CON": 2,
    #     "INT": 1,
    #     "WIS": 4,
    #     "CHA": 5
    # },
    "Monk": {
        "STR": 1,
        "DEX": 0,
        "CON": 2,
        "INT": 4,
        "WIS": 3,
        "CHA": 5
    },
    "Paladin": {
        "STR": 0,
        "DEX": 3,
        "CON": 2,
        "INT": 4,
        "WIS": 5,
        "CHA": 1
    },
    "Ranger": {
        "STR": 0,
        "DEX": 1,
        "CON": 2,
        "INT": 3,
        "WIS": 4,
        "CHA": 5
    },
    "Rogue": {
        "STR": 5,
        "DEX": 0,
        "CON": 1,
        "INT": 2,
        "WIS": 3,
        "CHA": 4
    },
    "Sorcerer": {
        "STR": 5,
        "DEX": 1,
        "CON": 2,
        "INT": 4,
        "WIS": 3,
        "CHA": 0
    },
    # "Summoner": {
    #     "STR": 5,
    #     "DEX": 1,
    #     "CON": 2,
    #     "INT": 4,
    #     "WIS": 3,
    #     "CHA": 0
    # },
    # "Warpriest": {
    #     "STR": 0,
    #     "DEX": 3,
    #     "CON": 2,
    #     "INT": 4,
    #     "WIS": 1,
    #     "CHA": 5
    # },
    "Wizard": {
        "STR": 5,
        "DEX": 3,
        "CON": 1,
        "INT": 0,
        "WIS": 2,
        "CHA": 4
    }
}
class_feats = json.load(
    open("pathfinder_class_feats.json", 'r'), encoding='utf-8')

# class_feats = json.load(open("5e_class_feats.json", 'r'), encoding='utf-8')


class PC(object):
    """Characters are the centerpiece of stories"""
    Name = Gender = Race = Appearance = Class = Feats = ''
    Traits = Story = []
    Age = Level = 0
    Spells = None
    Stats = []
    Weapon = [None, None]

    def __init__(self, new_char=None):
        if new_char is None:
            new_char = create_person(None)

        self.Name = new_char.Name
        self.Level = int(randint(1, 21))
        self.Race = new_char.Race
        self.Gender = new_char.Gender
        self.Age = new_char.Age
        self.Appearance = new_char.Appearance
        self.Traits = new_char.Traits
        self.Story = new_char.Story

        # First Roll
        self.roll()

        # Send the Rolls to determine the
        self.choose_class()

        self.Weapon = [
            Weapon(
                int(randint(0, 5)),
                iClass=choice([
                    'Heavy Axe', 'Light Axe', 'Heavy Blade', 'Light Blade',
                    'Close', 'Double', 'Flail', 'Hammer', 'Monk', 'Polearm',
                    'Spear'
                ])),
            Weapon(
                int(randint(0, 5)),
                iClass=choice(['Bows', 'Crossbow', 'Thrown']))
        ]

        # Spell enabled character - 1 in 3
        # if randint(3) == 0:
        # Spells for Classes that cast spells
        if self.Class in [
                'Bard', 'Cleric', 'Druid', 'Magus', 'Paladin', 'Ranger',
                'Sorcerer', 'Summoner', 'Warpriest', 'Wizard'
        ]:
            self.Spells = []
            for x in range(4 + self.Level * 2):
                s = choice(list(MasterSpells.keys()))
                if s not in self.Spells and MasterSpells[s][
                        'link'] not in MasterSpellBlacklist:
                    self.Spells.append(s)
            # Sort spells
            # self.Spells.sort(key=lambda x: MasterSpells[x]['school'])

    def roll(self):
        self.Stats = []
        for _ in range(6):
            temp = []
            for _ in range(4):
                temp.append(randint(1, 7))
            temp.sort(reverse=True)
            temp.pop()
            self.Stats.append(int(sum(temp)))

    def choose_class(self):
        self.Class = choice(list(playable.keys()))
        self.Stats.sort(reverse=True)
        self.Stats = [
            self.Stats[playable[self.Class]['STR']],
            self.Stats[playable[self.Class]['DEX']],
            self.Stats[playable[self.Class]['CON']],
            self.Stats[playable[self.Class]['INT']],
            self.Stats[playable[self.Class]['WIS']],
            self.Stats[playable[self.Class]['CHA']]
        ]

        for level in range(0, self.Level + 1):
            self.Feats += class_feats[self.Class][level]

    def __str__(self):
        info = self.Name + '<div><div class="bold text-md" style="text-indent: 50px">' + self.Class + ' ' + \
               str(self.Level) + '</div><ul><li><span style="font-weight:bold;">Race:</span> ' + self.Race + \
               '</li><li><span style="font-weight:bold;">Gender:</span> ' + self.Gender + \
               '</li><li><span style="font-weight:bold;">Age:</span> ' + str(self.Age) + \
               '</li><li><span style="font-weight:bold;">Appearance:</span> ' + str(self.Appearance) + \
               '</li><li><span style="font-weight:bold;">Trait 1:</span> ' + self.Traits[0] + "</li>"
        if len(self.Traits) > 1:
            info += '<li><span style="font-weight:bold;">Trait 2:</span> ' + self.Traits[
                1] + "</li>"
        info += "</ul><p>"
        for x in range(len(self.Story)):
            info += self.Story[x] + '</p>'
            if x + 1 < len(self.Story):
                info += '<p>'

        # Add Stats for Characters
        info += '<table class="inventory-table" style="width: 100%;"><tbody><tr><th>STR</th><th>DEX</th><th>CON' + \
                '</th><th>INT</th><th>WIS</th><th>CHA</th></tr><tr>'
        for s in self.Stats:
            b = -5 + int(s / 2)
            if b >= 0:
                add = '+' + str(b)
            else:
                add = str(b)
            info += '<td style="text-align: center;">' + str(
                s) + ' (' + add + ')</td>'
        info += '</tbody></table>'

        # Add Weapons
        info += '<ul style="columns: 2;padding: 10px;">'
        for weapon in self.Weapon:
            dam = '['
            for d in weapon.Damage:
                dam += '\'' + d + '\','
            dam += ']'
            info += '<table><td style="width: 50%"><span class="text-md">' + weapon.Name.title() + \
                    '</span><br /><span class="text-sm emp">' + weapon.Dice + ' (' + weapon.Crit + \
                    ') ' + dam + '</span></td></table><br/>'
        info += '</ul>'

        # Add Feats
        info += self.Feats
        info += "</tbody></table></br>"

        # Add Spells
        if self.Spells is not None:
            info += '<table class="inventory-table" style="width:100%;"><tr><th style="text-align:left;' \
                    'background-color:gray;color:white;padding:5px;">Spell</th><th style="text-align:left;' \
                    'background-color:gray;color:white;padding:5px;">Class</th><th style="text-align:left;' \
                    'background-color:gray;color:white;padding:5px;">Level</th></tr>'
            for spell in self.Spells:

                # pprint(MasterSpells[spell])
                level = MasterSpells[spell]['level'].split(' ')
                highlevel = 0
                for l in level:
                    m = re.match(r'(\d)', l)
                    if m is not None:
                        if int(m.group(1)) > highlevel:
                            highlevel = int(m.group(1))
                info += '<tr><td style="width:50%;"><span class="text-md"><a href="' + MasterSpells[spell]['link'] + \
                        '">' + spell + '</a></span></td><td>' + MasterSpells[spell]['school'].title() + '</td><td>' + \
                        str(highlevel) + '</td></tr>'
            info += '</table>'

        return info

    def from_dict(self, new_self):
        new_self.pop('Weapon')
        self.__dict__.update(new_self)

    def __iter__(self):
        for item in [
                self.Name, self.Gender, self.Race, self.Appearance, self.Class,
                self.Feats, self.Traits, self.Story, self.Age, self.Level,
                self.Spells, self.Stats, self.Weapon
        ]:
            yield item


if __name__ == '__main__':
    print(PC())
