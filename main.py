#!/usr/bin/python3
import town_generator


def make_sample():
    with open('generate.txt', 'w') as outf:
        # Write Weapon Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("2 0 4 15 20\n")
        # Write Armor Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("2 0 2 15 20\n")
        # Write Potion Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("1 0 9 10 15\n")
        # Write Enchant Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("1 0 9 10 15\n")
        # Write Enchanter Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("1 0 9 15 25\n")
        # Write Book Shop
        # [# of Stores, Quantity High, Quantity Low]
        outf.write("1 15 25\n")
        # Write Tavern Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("1 0 3 10 15\n")
        # Write Jewel Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High]
        outf.write("1 0 5 15 30\n")
        # Write Food Shop
        # [# of Stores, Rarity, Quantity Low, Quantity High]
        outf.write("1 0 15 30\n")
        # Write General Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Trinkets]
        outf.write("1 0 1 20 30 1")


if __name__ == '__main__':
    # Weapons = Armor = Potion = Enchant = Enchanter = Books = Tavern = Jewel = Food = General = []
    with open('generate.txt', 'r') as inf:
        """ Ordering
        Weapons|Armor|Potion|Enchant|Enchanter|Books|Tavern|Jewel|Food|General
        Each Line contains 5 variables
        [# of Stores, Rarity Low, Rarity High, Quan High, Quan Low]
        
        Different Ones: Books, Tavern
        Books: [# of Stores, Quan High, Quan Low]
        Tavern: [# of Stores, # of Rooms, Quantity of Items]
        """
        content = inf.readlines()
        val = content[0].split()
        Weapons = [int(thing) for thing in val]

        val = content[1].split()
        Armor = [int(thing) for thing in val]

        val = content[2].split()
        Potion = [int(thing) for thing in val]

        val = content[3].split()
        Enchant = [int(thing) for thing in val]

        val = content[4].split()
        Enchanter = [int(thing) for thing in val]

        val = content[5].split()
        Books = [int(thing) for thing in val]

        val = content[6].split()
        Tavern = [int(thing) for thing in val]

        val = content[7].split()
        Jewel = [int(thing) for thing in val]

        val = content[8].split()
        Food = [int(thing) for thing in val]

        val = content[9].split()
        General = [int(thing) for thing in val]

    town_generator.generate(Weapons, Armor, Potion, Enchant, Enchanter, Books, Tavern, Jewel, Food, General)


