from numpy.random import choice, randint
from resources import *
from stores import Weapon, Armor, Firearm


class Augment(object):
    """
    Cost should be in GP
    Rarity [0, 4] - Common, Uncommon, Rare, Very Rare, Legendary
        Rarity will also determine what types of material to use as well as the
            price for an item. Also note, that the prices are how much they cost
            to make, not the cost they'll be sold for.
    """
    Name = Spell = Class = Rarity = ""
    Level = Cost = Damage = 0
    Enchantment = Slot_Special = None
    Slots = ['Arm', 'Leg', 'Eye', 'Nose', 'Brain', 'Chest']

    def __init__(self, rare, iClass=None, iName=None):
        self.Rarity = rare
        # Pick the part to Augment
        if iClass is not None and iClass in self.Slots:
            self.Class = iClass
        else:
            self.Class = choice(self.Slots)

        m_name, m_info = self.__choose_material()

        if self.Class == 'Arm' and randint(4) == 1:
            self.Slot_Special = Firearm(self.Rarity)
            self.Name = self.Slot_Special.Name + " Arm"

        elif self.Class == 'Arm':
            self.Slot_Special = Weapon(
                self.Rarity, iClass=choice(list(possible_melee.keys())))
            self.Name = self.Slot_Special.Name + " Arm"

        elif self.Class == 'Leg':
            nam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                   13][self.Rarity:self.Rarity + 9]
            self.Slot_Special = str(
                choice(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
                    ][self.Rarity:self.Rarity + 9],
                    p=[
                        0.360000001, 0.252839506, 0.169382716, 0.106666667,
                        0.061728395, 0.031604938, 0.013333333, 0.003950617,
                        0.000493827
                    ]) * 10)
            self.Slot_Special = '+' + self.Slot_Special + ' Base Movement Speed'
            self.Name = m_name + ' Legs'

        elif self.Class == 'Eye':
            self.Slot_Special = str(
                choice(
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
                    ][self.Rarity:self.Rarity + 9],
                    p=[
                        0.360000001, 0.252839506, 0.169382716, 0.106666667,
                        0.061728395, 0.031604938, 0.013333333, 0.003950617,
                        0.000493827
                    ]) * 10) + " "
            self.Name = m_name + ' Optical Implant'

            if self.Rarity < 2:
                self.Slot_Special += ' ft. Darkvision'
            elif self.Rarity < 4:
                self.Slot_Special += ' ft. Thermal'
            elif self.Rarity == 4:
                self.Slot_Special = str(eval(self.Slot_Special) - 40)
                self.Slot_Special += ' ft. True Sight'

        elif self.Class == 'Nose':
            self.Slot_Special = ""

        elif self.Class == 'Brain':
            num = str(
                choice(
                    [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9,
                     9][self.Rarity:self.Rarity + 9],
                    p=[
                        0.360000001, 0.252839506, 0.169382716, 0.106666667,
                        0.061728395, 0.031604938, 0.013333333, 0.003950617,
                        0.000493827
                    ]))
            self.Slot_Special = "+" + num + " " + choice(
                ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'])
            self.Name = m_name + " " + self.Class + " Implant"

        elif self.Class == 'Chest':
            self.Slot_Special = Armor(self.Rarity, iName="")
            self.Name = self.Slot_Special.Name + " Natural Armor"

        # Are there potential Add-ins?
        self.__add_ins()

        # Change name if necessary
        if iName is not None:
            self.Name = iName

    def __choose_material(self):
        while True:
            if self.Rarity == 1:  # Uncommon Materials
                material_name = choice(list(uncommon_material.keys()))
                material_stats = uncommon_material[material_name]
            elif self.Rarity == 2:  # Rare Materials
                material_name = choice(list(rare_material.keys()))
                material_stats = rare_material[material_name]
            elif self.Rarity == 3:  # Very Rare Materials
                material_name = choice(list(very_rare_material.keys()))
                material_stats = very_rare_material[material_name]
            elif self.Rarity == 4:  # Legendary Materials
                material_name = choice(list(legendary_material.keys()))
                material_stats = legendary_material[material_name]
            else:  # Common Materials
                material_name = choice(list(common_material.keys()))
                material_stats = common_material[material_name]
            # Validate correct material
            if 'HA' in material_stats['Type']:
                break
        return material_name, material_stats

    def __add_ins(self):
        pass

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = float(self.Cost + self.Enchantment.Cost)
        else:
            print("This Item is already enchanted.")

    def __str__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    from numpy.matlib import median, average

    for i in range(5):
        for s in ['Arm', 'Leg', 'Eye', 'Nose', 'Brain', 'Chest']:
            print(Augment(i, iClass=s))
        print()

    # for i in range(5):
    #     data = []
    #     for x in range(1000):
    #         a = Augment(i, 'Eye')
    #         data.append(eval(a.Slot_Special[0:3]))
    #     print("_______________", i, "____________________")
    #     print("AVG:", average(data))
    #     print("MED:", median(data))
    #     print("MIN:", min(data))
    #     print("MAX:", max(data))
