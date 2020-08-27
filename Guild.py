from quests import Quest
from numpy.random import choice, randint
from character import create_person
from variance import create_variance
from PC import PC
from stores import Art, General, Book, Weapon, Armor, Scroll, Potion, Wand


class Guild:
    Type = ''
    Members = Leaders = Inventory = []
    Quantity = 0
    possible_guilds = ['magic', 'school', 'merchant', 'bounty', 'martial']

    def __init__(self, t, l, m, q):
        if t not in self.possible_guilds:
            self.Type = choice(self.possible_guilds)
        else:
            self.Type = t
        self.Quantity = q

        for _ in range(randint(l[0], l[1])):
            self.Leaders.append(PC())

        for _ in range(randint(m[0], m[1])):
            self.Members.append(create_person(create_variance()))

        self.fill_inventory()

    def fill_inventory(self):
        self.Inventory = []
        for _ in range(self.Quantity):
            if self.Type == 'magic':
                if randint(0, 2) == 0:
                    self.Inventory.append(Potion(randint(0, 10)))
                else:
                    self.Inventory.append(Wand(randint(0, 10)))
            elif self.Type == 'school':
                self.Inventory.append(Scroll(randint(0, 10), naming=False))
            elif self.Type == 'merchant':
                r = randint(0, 3)
                if r == 1:
                    self.Inventory.append(Art(randint(0, 6)))
                elif r == 2:
                    self.Inventory.append(
                        General(
                            randint(0, 6),
                            trinket=True if randint(0, 2) == 0 else False))
                else:
                    self.Inventory.append(Book(randint(0, 6)))
            elif self.Type == 'bounty':
                self.Inventory.append(Quest(randint(1, 21)))
            elif self.Type == 'martial':
                if randint(0, 2) == 0:
                    self.Inventory.append(Weapon(randint(0, 5)))
                else:
                    self.Inventory.append(Armor(randint(0, 5)))

    def from_dict(self, new_self):
        self.__dict__.update(new_self)
        self.fill_inventory()

    def __str__(self):
        return ''
