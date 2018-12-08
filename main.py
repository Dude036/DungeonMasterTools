#!/usr/bin/python3
import town_generator
from PC import PC
from os import linesep
from re import match

"""
@TODO:
1: UNIT TESTS!
2: Try sorting items in stores based on rarity.
3: Character creator with actual classes
4: Add Beasts to Beast list
5: Just treasure printing
"""


def make_sample():
    with open('generate.txt', 'w') as outf:
        # Write Weapon Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("2 0 4 15 20 1.0" + linesep)
        # Write Armor Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("2 0 2 15 20 1.0" + linesep)
        # Write Potion Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 10 15 1.0" + linesep)
        # Write Enchant Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 10 15 1.0" + linesep)
        # Write Enchanter Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 9 15 25 1.0" + linesep)
        # Write Book Shop
        # [# of Stores, Quantity High, Quantity Low, Inflation]
        outf.write("1 15 25 1.0" + linesep)
        # Write Tavern Shop
        # [# of Stores, Rooms, Food Quantity Low, Food Quantity High, Inflation]
        outf.write("1 3 10 15 1.0" + linesep)
        # Write Jewel Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 5 15 30 1.0" + linesep)
        # Write Food Shop
        # [# of Stores, Quantity Low, Quantity High, Inflation]
        outf.write("1 15 30 1.0" + linesep)
        # Write General Shop
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Trinkets, Inflation]
        outf.write("1 0 1 20 30 1 1.0" + linesep)
        # Write Brothel
        # [# of Stores, Quantity Low, Quantity High, Inflation]
        outf.write("1 5 10 1.0" + linesep)
        # Write Gunsmith
        # [# of Stores, Rarity Low, Rarity High, Quantity Low, Quantity High, Inflation]
        outf.write("1 0 5 15 30 1.0" + linesep)
        # Write Quest board
        # [# of Stores, Level Low, Level High, Quantity]
        outf.write("1 0 5 20")


def make_sample_input():
    store_dict = {'Weapon': r'(\d+) ([01234]) ([01234]) (\d+) (\d+) ([\d.]+)',
                  'Armor': r'(\d+) ([01234]) ([01234]) (\d+) (\d+) ([\d.]+)',
                  'Potion': r'(\d+) (\d) (\d) (\d+) (\d+) ([\d.]+)',
                  'Enchantment': r'(\d+) (\d) (\d) (\d+) (\d+) ([\d.]+)',
                  'Enchanter': r'(\d+) (\d) (\d) (\d+) (\d+) ([\d.]+)',
                  'Book': r'(\d+) (\d+) (\d+) ([\d.]+)',
                  'Tavern': r'(\d+) (\d+) (\d+) ([\d.]+)',
                  'Jeweller': r'(\d+) (\d) (\d) (\d+) (\d+) ([\d.]+)',
                  'Restaurant': r'(\d+) (\d+) (\d+) ([\d.]+)',
                  'General': r'(\d+) ([0123]) ([0123]) (\d+) (\d+) \d+ ([\d.]+)',
                  'Brothel': r'(\d+) (\d+) (\d+) ([\d.]+)',
                  'Gunsmith': r'(\d+) ([01234]) ([01234]) (\d+) (\d+) ([\d.]+)',
                  'Quest Board': r'(\d+) \d+ \d+ \d+'}

    with open('generate.txt', 'w') as outf:
        for store in list(store_dict.keys()):
            invalid_input = True
            user_input = ''
            while invalid_input:
                user_input = input("Please input information for " + store + ' store:\n')
                parsed = match(store_dict[store], user_input)
                print([int(p) for p in parsed.groups()])
                if parsed is None:
                    print("Invalid input for", store, '. Please see README for more info.')
                    continue
                elif store == 'Quest Board' and int(parsed.group(2)) > 20 and int(parsed.group(3)) > 20:
                    print("Too large of level for", store, '. Please see README for more info.')
                    continue
                elif store in ['Weapon', 'Armor', 'Potion', 'Enchantment', 'Enchanter', 'Jeweller', 'General',
                               'Gunsmith', 'Quest Board'] and int(parsed.group(2)) > int(parsed.group(3)):
                    print("Rarity lower bound higher than upper bound.")
                    continue
                elif store in ['Weapon', 'Armor', 'Potion', 'Enchantment', 'Enchanter', 'Jeweller', 'General',
                               'Gunsmith'] and int(parsed.group(4)) > int(parsed.group(5)):
                    print("Quantity lower bound higher than upper bound.")
                    continue
                elif store in ['Weapon', 'Armor', 'Potion', 'Enchantment', 'Enchanter', 'Jeweller', 'General',
                               'Gunsmith'] and int(parsed.group(4)) > int(parsed.group(5)):
                    print("Quantity lower bound higher than upper bound.")
                    continue
                elif store in ['Weapon', 'Armor', 'Potion', 'Enchantment', 'Enchanter', 'Jeweller', 'General',
                               'Gunsmith'] and eval(parsed.group(6)) <= 0:
                    print("Inflation rate cannot be below 0.0.")
                    continue
                elif store == 'Books' and eval(parsed.group(4)) <= 0:
                    print("Inflation rate cannot be below 0.0.")
                    continue
                elif store == 'Tavern' and eval(parsed.group(4)) <= 0:
                    print("Inflation rate cannot be below 0.0.")
                    continue
                elif store == 'Restaurant' and eval(parsed.group(4)) <= 0:
                    print("Inflation rate cannot be below 0.0.")
                    continue
                elif store == 'Brothel' and eval(parsed.group(4)) <= 0:
                    print("Inflation rate cannot be below 0.0.")
                    continue
                else:
                    invalid_input = False
            outf.write(user_input + '\n')

        user_input = ''
        while user_input == '':
            print()
            user_input = input("Add characters. Type their title here. If you want them to be and NPC with items " + \
                               "and stats, preface with an '!'.")
            if user_input == "":
                break
            else:
                outf.write(user_input + '\n')


if __name__ == '__main__':
    # Weapons = Armor = Potion = Enchant = Enchanter = Books = Tavern = Jewel = Food = General = []
    with open('generate.txt', 'r') as inf:
        """ Ordering
        Weapons|Armor|Potion|Enchant|Enchanter|Books|Tavern|Jewel|Food|General|Brothel
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

        val = content[11].split()
        Gunsmith = [eval(thing) for thing in val]

        val = content[12].split()
        Quests = [eval(thing) for thing in val]

        Positions = []
        NPC = []

        for thing in range(13, len(content)):
            title = content[thing].strip()
            if title[0] == '!':
                NPC.append(title[1:])
            else:
                Positions.append(title)

    town_name = town_generator.generate(Weapons, Armor, Potion, Enchant, Enchanter, Books, Tavern, Jewel, Food, General,
                                        Brothel, Gunsmith, Quests)
    for p in Positions:
        town_generator.write_people(town_generator.create_person(town_generator.create_variance()), p)
    for npc in NPC:
        town_generator.write_npc(PC(), npc)
    print("Writing the town ", town_name)
    town_generator.write_html(town_name)
