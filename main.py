#!/usr/bin/python3
import town_generator

"""
@TODO:
1: Brothel?
2: UNIT TESTS!
"""


def make_sample():
    with open('generate.txt', 'w') as outf:
        # Write Weapon Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("2 0 4 15 20 1.0\r\n")
        # Write Armor Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("2 0 2 15 20 1.0\r\n")
        # Write Potion Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 10 15 1.0\r\n")
        # Write Enchant Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 10 15 1.0\r\n")
        # Write Enchanter Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 15 25 1.0\r\n")
        # Write Book Shop
        # [# of Stores, Quantity High, Quantity Low, Inflation]
        outf.write("1 15 25 1.0\r\n")
        # Write Tavern Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 3 10 15 1.0\r\n")
        # Write Jewel Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 5 15 30 1.0\r\n")
        # Write Food Shop
        # [# of Stores, Rarity, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 15 30 1.0\r\n")
        # Write General Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Trinkets, Inflation]
        outf.write("1 0 1 20 30 1 1.0\r\n")
        # Write Brothel
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 5 10 1")

if __name__ == '__main__':
    # Weapons = Armor = Potion = Enchant = Enchanter = Books = Tavern = Jewel = Food = General = []
    with open('generate.txt', 'r') as inf:
        """ Ordering
        Weapons|Armor|Potion|Enchant|Enchanter|Books|Tavern|Jewel|Food|General
        See above for explanation and creation of the settings
        """
        content = inf.readlines()
        val = content[0].split()
        Weapons = [eval(thing) for thing in val]

        val = content[1].split()
        Armor = [eval(thing) for thing in val]

        val = content[2].split()
        Potion = [eval(thing) for thing in val]

        val = content[3].split()
        Enchant = [eval(thing) for thing in val]

        val = content[4].split()
        Enchanter = [eval(thing) for thing in val]

        val = content[5].split()
        Books = [eval(thing) for thing in val]

        val = content[6].split()
        Tavern = [eval(thing) for thing in val]

        val = content[7].split()
        Jewel = [eval(thing) for thing in val]

        val = content[8].split()
        Food = [eval(thing) for thing in val]

        val = content[9].split()
        General = [eval(thing) for thing in val]

        val = content[10].split()
        Brothel = [eval(thing) for thing in val]

        Positions = []
        for thing in range(11, len(content)):
            Positions.append(content[thing].strip())

    town_name = town_generator.generate(Weapons, Armor, Potion, Enchant, Enchanter, Books, Tavern, Jewel, Food, General,
                                        Brothel)
    for p in Positions:
        town_generator.write_people(town_generator.create_person(town_generator.create_variance()), p)
    print("Writing the town ", town_name)
    town_generator.write_html(town_name)
