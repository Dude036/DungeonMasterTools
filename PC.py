#!/usr/bin/python3

from numpy.random import randint, choice
from character import Character, create_person
from spell_list import MasterSpells
from stores import Weapon
from pprint import pprint
import re


class PC(Character):
    """Characters are the centerpiece of stories"""
    Name = Gender = Race = Appearance = ''
    Traits = Story = []
    Age = Level = 0
    Spells = None
    Stats = []
    Weapon = [None, None]

    def __init__(self, newName=None):
        super(Character, self).__init__()
        c = create_person(None)

        self.Level = randint(1, 21)
        if newName is None:
            self.Name = c.Name
        else:
            self.Name = newName
        self.Race = c.Race
        self.Gender = c.Gender
        self.Age = c.Age
        self.Appearance = c.Appearance
        self.Traits = c.Traits
        self.Story = c.Story

        self.roll()

        self.Weapon = [Weapon(randint(0, 5),
                              iClass=choice(['Heavy Axe', 'Light Axe', 'Heavy Blade', 'Light Blade', 'Close', 'Double',
                                             'Flail', 'Hammer', 'Monk', 'Polearm', 'Spear'])),
                       Weapon(randint(0, 5),
                              iClass=choice(['Bows', 'Crossbow', 'Thrown']))]

        # Spell enabled character - 1 in 3
        if randint(3) == 0:
            self.Spells = []
            for x in range(4 + self.Level * 2):
                s = choice(list(MasterSpells.keys()))
                if s not in self.Spells:
                    self.Spells.append(s)
            # Sort spells
            self.Spells.sort(key=lambda x: MasterSpells[x]['school'])

    def roll(self):
        self.Stats = []
        for _ in range(6):
            temp = []
            for _ in range(4):
                temp.append(randint(1, 7))
            temp.sort(reverse=True)
            temp.pop()
            self.Stats.append(sum(temp))

    def __str__(self):
        info = self.Name + '<div>' + \
               '<ul><li><span style="font-weight:bold;">Race:</span> ' + self.Race + \
               '</li><li><span style="font-weight:bold;">Gender:</span> ' + self.Gender + \
               '</li><li><span style="font-weight:bold;">Age:</span> ' + str(self.Age) + \
               '</li><li><span style="font-weight:bold;">Appearance:</span> ' + str(self.Appearance) + \
               '</li><li><span style="font-weight:bold;">Trait 1:</span> ' + self.Traits[0] + "</li>"
        if len(self.Traits) > 1:
            info += '<li><span style="font-weight:bold;">Trait 2:</span> ' + self.Traits[1] + "</li>"
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
            info += '<td style="text-align: center;">' + str(s) + ' (' + add + ')</td>'
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

        # Add Spells
        if self.Spells is not None:
            info += '</ul><table class="inventory-table" style="width:100%;"><tr><th style="text-align:left;' \
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


if __name__ == '__main__':
    print(PC())

