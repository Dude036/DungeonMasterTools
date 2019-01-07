#!/usr/bin/python3
import town_generator
from PC import PC
from os import linesep
from re import match
import simplejson as json
"""
@TODO:
1: UNIT TESTS!
2: Try sorting items in stores based on rarity.
3: Character creator with actual classes
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
    store_dict = {
        'Weapon': r'(\d+) ([01234]) ([01234]) (\d+) (\d+) ([\d.]+)',
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
        'Quest Board': r'(\d+) \d+ \d+ \d+'
    }

    with open('generate.txt', 'w') as outf:
        for store in list(store_dict.keys()):
            invalid_input = True
            user_input = ''
            while invalid_input:
                user_input = input("Please input information for " + store +
                                   ' store:\n')
                parsed = match(store_dict[store], user_input)
                print([int(p) for p in parsed.groups()])
                if parsed is None:
                    print("Invalid input for", store,
                          '. Please see README for more info.')
                    continue
                elif store == 'Quest Board' and int(
                        parsed.group(2)) > 20 and int(parsed.group(3)) > 20:
                    print("Too large of level for", store,
                          '. Please see README for more info.')
                    continue
                elif store in [
                        'Weapon', 'Armor', 'Potion', 'Enchantment',
                        'Enchanter', 'Jeweller', 'General', 'Gunsmith',
                        'Quest Board'
                ] and int(parsed.group(2)) > int(parsed.group(3)):
                    print("Rarity lower bound higher than upper bound.")
                    continue
                elif store in [
                        'Weapon', 'Armor', 'Potion', 'Enchantment',
                        'Enchanter', 'Jeweller', 'General', 'Gunsmith'
                ] and int(parsed.group(4)) > int(parsed.group(5)):
                    print("Quantity lower bound higher than upper bound.")
                    continue
                elif store in [
                        'Weapon', 'Armor', 'Potion', 'Enchantment',
                        'Enchanter', 'Jeweller', 'General', 'Gunsmith'
                ] and int(parsed.group(4)) > int(parsed.group(5)):
                    print("Quantity lower bound higher than upper bound.")
                    continue
                elif store in [
                        'Weapon', 'Armor', 'Potion', 'Enchantment',
                        'Enchanter', 'Jeweller', 'General', 'Gunsmith'
                ] and eval(parsed.group(6)) <= 0:
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
    generator = json.loads(open('generate.json', 'r').read())
    Weapons = [
        generator['Weapon Shops']["# of Stores"],
        generator['Weapon Shops']["Rarity Low"],
        generator['Weapon Shops']["Rarity High"],
        generator['Weapon Shops']["Quantity Low"],
        generator['Weapon Shops']["Quantity High"],
        generator['Weapon Shops']["Inflation"]
    ]
    Armor = [
        generator['Armor Shops']["# of Stores"],
        generator['Armor Shops']["Rarity Low"],
        generator['Armor Shops']["Rarity High"],
        generator['Armor Shops']["Quantity Low"],
        generator['Armor Shops']["Quantity High"],
        generator['Armor Shops']["Inflation"]
    ]
    Potion = [
        generator["Potion Shops"]["# of Stores"],
        generator["Potion Shops"]["Rarity Low"],
        generator["Potion Shops"]["Rarity High"],
        generator["Potion Shops"]["Quantity Low"],
        generator["Potion Shops"]["Quantity High"],
        generator["Potion Shops"]["Inflation"]
    ]
    Enchant = [
        generator['Enchant Shops']["# of Stores"],
        generator['Enchant Shops']["Rarity Low"],
        generator['Enchant Shops']["Rarity High"],
        generator['Enchant Shops']["Quantity Low"],
        generator['Enchant Shops']["Quantity High"],
        generator['Enchant Shops']["Inflation"]
    ]
    Enchanter = [
        generator["Enchanter Shops"]["# of Stores"],
        generator["Enchanter Shops"]["Rarity Low"],
        generator["Enchanter Shops"]["Rarity High"],
        generator["Enchanter Shops"]["Quantity Low"],
        generator["Enchanter Shops"]["Quantity High"],
        generator["Enchanter Shops"]["Inflation"]
    ]
    Books = [
        generator["Book Shops"]["# of Stores"],
        generator["Book Shops"]["Quantity Low"],
        generator["Book Shops"]["Quantity High"],
        generator["Book Shops"]["Inflation"]
    ]
    Tavern = [
        generator["Tavern Shops"]["# of Stores"],
        generator["Tavern Shops"]["Rooms"],
        generator["Tavern Shops"]["Quantity Low"],
        generator["Tavern Shops"]["Quantity High"],
        generator["Tavern Shops"]["Inflation"]
    ]
    Jewel = [
        generator["Jewel Shops"]["# of Stores"],
        generator["Jewel Shops"]["Rarity Low"],
        generator["Jewel Shops"]["Rarity High"],
        generator["Jewel Shops"]["Quantity Low"],
        generator["Jewel Shops"]["Quantity High"],
        generator["Jewel Shops"]["Inflation"]
    ]
    Food = [
        generator["Food Shops"]["# of Stores"],
        generator["Food Shops"]["Quantity Low"],
        generator["Food Shops"]["Quantity High"],
        generator["Food Shops"]["Inflation"]
    ]
    General = [
        generator["General Shops"]["# of Stores"],
        generator["General Shops"]["Rarity Low"],
        generator["General Shops"]["Rarity High"],
        generator["General Shops"]["Quantity Low"],
        generator["General Shops"]["Quantity High"],
        generator["General Shops"]["Trinkets"],
        generator["General Shops"]["Inflation"]
    ]
    Brothel = [
        generator["Brothels"]["# of Stores"],
        generator["Brothels"]["Quantity Low"],
        generator["Brothels"]["Quantity High"],
        generator["Brothels"]["Inflation"]
    ]
    Gunsmith = [
        generator["Gunsmiths"]["# of Stores"],
        generator["Gunsmiths"]["Rarity Low"],
        generator["Gunsmiths"]["Rarity High"],
        generator["Gunsmiths"]["Quantity Low"],
        generator["Gunsmiths"]["Quantity High"],
        generator["Gunsmiths"]["Inflation"]
    ]
    Quests = [
        generator["Quest Boards"]["# of Stores"],
        generator["Quest Boards"]["Level Low"],
        generator["Quest Boards"]["Level High"],
        generator["Quest Boards"]["Quantity"]
    ]

    town_name = town_generator.generate(Weapons, Armor, Potion, Enchant,
                                        Enchanter, Books, Tavern, Jewel, Food,
                                        General, Brothel, Gunsmith, Quests)

    for p in generator['Occupations']:
        town_generator.write_people(
            town_generator.create_person(town_generator.create_variance()), p)
    for npc in generator['NPCs']:
        town_generator.write_npc(PC(), npc)

    print("Writing the town ", town_name)
    town_generator.write_html(town_name)
