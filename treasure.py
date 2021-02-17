#!/usr/bin/python3
import re
from numpy.random import randint, choice
from stores import Jewel, Art, Scroll, Ring, Wondrous, Weapon, Armor, Potion, determine_cost

Monster_Types = {
    "aberration": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
    ],
    "animal": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
    ],
    "beast": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
    ],
    "celestial": [
        'Coins',
        'Coins and Gems',
        'Art Objects',
        'Coins & Small Objects',
        'Combatant Gear',
        'Spellcaster Gear',
        'Lair Treasure',
        'Treasure Horde',
    ],
    "construct": [
        'Coins and Gems',
        'Art Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Lair Treasure',
    ],
    "dragon": [
        'Coins',
        'Coins and Gems',
        'Art Objects',
        'Lair Treasure',
        'Treasure Horde',
    ],
    "elemental": [
        'Coins & Small Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Spellcaster Gear',
        'Lair Treasure',
    ],
    "fey": [
        'Coins and Gems',
        'Art Objects',
        'Coins & Small Objects',
        'Spellcaster Gear',
    ],
    "fiend": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Spellcaster Gear',
        'Lair Treasure',
    ],
    "giant": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Spellcaster Gear',
        'Lair Treasure',
    ],
    "humanoid": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Spellcaster Gear',
        'Lair Treasure',
    ],
    "magical beast": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
    ],
    "monstrosity": [
        'Coins',
        'Coins and Gems',
        'Art Objects',
        'Coins & Small Objects',
        'Armor and weapons',
        'Lair Treasure',
    ],
    "monstrous humanoid": [
        'Coins',
        'Coins and Gems',
        'Art Objects',
        'Coins & Small Objects',
        'Armor and weapons',
        'Lair Treasure',
    ],
    "ooze": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
    ],
    "outsider": [
        'Coins',
        'Coins and Gems',
        'Art Objects',
        'Coins & Small Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Spellcaster Gear',
        'Lair Treasure',
        'Treasure Horde',
    ],
    "plant": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
    ],
    "undead": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
        'Armor and weapons',
        'Combatant Gear',
        'Spellcaster Gear',
    ],
    "vermin": [
        'Coins',
        'Coins and Gems',
        'Coins & Small Objects',
    ],
}
Coins = {
    1: ['10d4 *2 cp', "4d4 sp"],
    5: ['6d10 *4 cp', "3d8 *2 sp", "6d10 *4 cp"],
    10: ['6d20 *4 cp', '5d10 *2 sp', '2d10 gp'],
    25: ["6d6 *10 cp", "3d6 *5 sp", "3d4 *2 gp"],
    50: ["8d8 gp", "4d6 *6 sp", "5d12 *14 cp"],
    100: ["9d8 *5 sp", "18d10 gp"],
    200: ["2d4 *20 sp", "3d8 *4 gp", "2d4 *2 pp"],
    500: ["9d10 *3 gp", "3d8 *2 pp"],
    1000: ["6d8 *6 gp", "4d12 *2 pp"],
    5000: ["17d8 *8 gp", "9d12 *3 pp"],
    10000: ["10d20 *10 gp", "9d12 *4 pp"],
    50000: ["5d8 *50 gp", "8d10 *10 pp"],
}
Coins_and_Gems = {
    1: ['10d4 *2 cp', "4d4 sp"],
    5: ['6d10 *4 cp', "3d8 *2 sp", "6d10 *4 cp"],
    10: ["grade 1 gemstone"],
    25: ["6d6 *10 cp", "3d6 *5 sp", "3d4 *2 gp", "2 grade 1 gemstones"],
    50: ["grade 2 gemstone"],
    100: ["grade 3 gemstone"],
    150: ["grade 2 gemstone", "grade 3 gemstone"],
    200: [
        "2d4 *20 sp", "3d8 *4 gp", "2d4 *2 pp", "4 grade 1 gemstones",
        "grade 3 gemstone"
    ],
    250: ["2 grade 2 gemstones", "grade 3 gemstone"],
    500: ["9d10 *3 gp", "3d8 *2 pp", "grade 4 gemstone"],
    1000: ["6d8 *6 gp", "4d12 *2 pp", "grade 5 gemstone"],
    2500: ["2 grade 4 gemstones", "grade 5 gemstone"],
    5000: ["17d8 *8 gp", "9d12 *3 pp", "grade 6 gemstone"],
    10000:
    ["10d20 *10 gp", "9d12 *4 pp", "5 grade 5 gemstones", "grade 6 gemstone"],
    20000: ["3 grade 6 gemstones"],
    50000: [
        "5d8 *50 gp", "8d10 *10 pp", "10 grade 3 gemstones",
        "4 grade 4 gemstones", "6 grade 5 gemstones", "8 grade 6 gemstones"
    ],
}
Art_Objects = {
    1: ["4d4 sp"],
    50: ["grade 1 art object"],
    100: ["grade 2 art object"],
    150: ["grade 1 art object", "grade 2 art object"],
    200: ["2 grade 2 art objects"],
    250: ["3 grade 1 art objects", "grade 2 art object"],
    500: ["grade 3 art object"],
    750:
    ["3 grade 1 art objects", "2 grade 2 art objects", "grade 3 art object"],
    1000: ["grade 4 art object"],
    1500: ["grade 3 art object", "grade 4 art object"],
    2000: ["2 grade 4 art objects"],
    2500:
    ["5 grade 2 art objects", "2 grade 3 art objects", "grade 4 art object"],
    5000: ["grade 5 art object"],
    7500: ["grade 3 art object", "2 grade 4 art objects", "grade 5 art object"],
    10000: ["grade 6 art object"],
    15000: ["grade 5 art object", "grade 6 art object"],
    20000: ["2 grade 5 art objects", "grade 6 art object"],
    50000: [
        "10 grade 3 art objects", "5 grade 4 art objects",
        "4 grade 5 art objects", "2 grade 6 art objects"
    ],
}
Coins_and_Objects = {
    1: ["4d4 sp"],
    5: [
        '6d10 *4 cp',
        "3d8 *2 sp",
        "6d10 *4 cp",
    ],
    40: ["lesser minor scroll"],
    50: ["8d8 gp", "4d6 *6 sp", "5d12 *14 cp", "lesser minor potion"],
    100:
    ["9d8 *5 sp", "18d10 gp", "lesser minor potion", "lesser minor scroll"],
    150: ["greater minor scroll"],
    200: [
        "2d4 *20 sp", "3d8 *4 gp", "2d4 *2 pp", "greater minor potion",
        "lesser minor scroll"
    ],
    250: ["2 lesser minor potions", "greater minor scroll"],
    300: ["greater minor potion", "greater minor scroll"],
    400: ["greater minor potion", "2 greater minor scrolls"],
    450: ["lesser medium potion", "greater minor scroll"],
    500: [
        "9d10 *3 gp", "3d8 *2 pp", "2 greater minor potions",
        "greater minor scroll"
    ],
    750: ["greater minor scroll", "lesser minor wand"],
    1000:
    ["6d8 *6 gp", "4d12 *2 pp", "lesser medium potion", "lesser medium scroll"],
    1250: ["lesser medium potion", "lesser minor wand"],
    1500: ["greater minor wand"],
    1750: ["greater medium potion", "greater medium scroll"],
    2000: ["greater medium potion", "greater minor wand"],
    2500: ["lesser medium potion", "2 greater medium scrolls"],
    3000:
    ["greater medium potion", "greater medium scroll", "greater minor wand"],
    4000: ["greater medium scroll", "2 greater minor wands"],
    5000: [
        "17d8 *8 gp", "9d12 *3 pp", "3 lesser major potions",
        "2 greater medium scrolls", "greater minor wand"
    ],
    7500: ["lesser major scroll", "lesser medium wand"],
    8000: ["2 greater major potions", "2 greater major scrolls"],
    10000: ["10d20 *10 gp", "9d12 *4 pp", "greater medium wand"],
    12500: [
        "greater major potion", "greater major scroll", "lesser medium wand"
    ],
    15000: ["lesser major wand"],
    17500: [
        "3 greater major potions", "2 lesser major scrolls",
        "greater medium wand"
    ],
    20000: [
        "2 greater major potions", "greater major scroll", "lesser major wand"
    ],
    22500: ["3 lesser major potions", "greater major wand"],
    25000: ["5 greater major scrolls", "greater medium wand"],
    30000: [
        "4 greater major potions", "3 greater major scrolls",
        "greater major wand"
    ],
    50000: [
        "5d8 *50 gp", "8d10 *10 pp", "4 greater major scrolls",
        "2 greater major wands"
    ],
}
Armor_and_Weapons = {
    1: ["4d4 sp"],
    200: ["masterwork light armor"],
    300: ["masterwork medium armor"],
    350: ["masterwork weapon"],
    1000: ["masterwork heavy armor"],
    1500: ["lesser minor armor"],
    2500: ["lesser minor weapon"],
    3000: ["greater minor armor"],
    3500: [
        "masterwork medium armor", "masterwork light armor",
        "lesser medium weapon"
    ],
    4000: ["lesser minor armor", "lesser minor weapon"],
    5500: ["greater minor armor", "lesser minor weapon"],
    6000: ["greater minor weapon"],
    7500: ["lesser minor armor", "greater minor weapon"],
    8000: ["greater minor armor", "2 lesser minor weapons"],
    9000: ["greater minor armor", "greater minor weapon"],
    10000: ["lesser medium armor", "lesser minor weapon"],
    13000: ["lesser medium weapon"],
    13500: ["lesser medium armor", "greater medium weapon"],
    15000: ["greater medium armor", "lesser minor weapon"],
    20000: ["lesser medium armor", "lesser medium weapon"],
    25000: ["greater minor armor", "greater medium weapon"],
    30000:
    ["lesser major armor", "lesser minor weapon", "greater minor weapon"],
    32500: ["lesser medium armor", "greater medium weapon"],
    35000: ["lesser major armor", "lesser medium weapon"],
    37500: ["lesser medium armor", "lesser major weapon"],
    40000: ["greater major armor", "greater minor weapon"],
    50000: ["greater major armor", "lesser medium weapon"],
    75000: ["greater minor armor", "greater major weapon"],
    100000: ["greater major armor", "greater major weapon"],
}
Combatant_Gear = {
    1: ["4d4 sp"],
    50: ["lesser minor potion"],
    250: ["masterwork light armor", "lesser minor potion"],
    350: ["masterwork medium armor", "lesser minor potion"],
    400: ["masterwork weapon", "lesser minor potion"],
    500: ["masterwork weapon", "greater minor potion"],
    750:
    ["masterwork medium armor", "masterwork weapon", "2 lesser minor potions "],
    1000: ["masterwork heavy armor"],
    1500:
    ["masterwork heavy armor", "masterwork weapon", "greater minor potion"],
    2000:
    ["lesser minor armor", "masterwork weapon", "2 greater minor potions "],
    3000: [
        "masterwork medium armor", "lesser minor weapon", "greater minor potion"
    ],
    4000: [
        "lesser minor armor", "masterwork weapon", "lesser minor wondrous item",
        "greater minor potion"
    ],
    5000: [
        "masterwork medium armor", "lesser minor weapon",
        "lesser minor wondrous item", "greater minor potion"
    ],
    6000:
    ["lesser minor armor", "lesser minor weapon", "lesser minor wondrous item"],
    7500: ["greater minor armor", "lesser minor weapon", "lesser minor ring"],
    10000: [
        "greater minor armor", "lesser minor weapon", "lesser minor ring",
        "lesser minor wondrous item", "3 greater minor potions "
    ],
    11000: [
        "greater minor armor", "greater medium weapon",
        "2 greater medium potions "
    ],
    12500: [
        "greater minor armor", "lesser minor weapon",
        "greater minor wondrous item", "2 greater medium potions "
    ],
    15000: [
        "greater minor armor", "greater minor weapon", "greater minor ring"
    ],
    20000: [
        "lesser medium armor", "greater minor weapon",
        "greater minor wondrous item", "2 greater medium potions "
    ],
    25000: [
        "lesser medium armor", "lesser medium weapon", "lesser minor ring",
        "lesser minor wondrous item", "2 greater medium potions"
    ],
    30000: [
        "lesser medium armor", "lesser medium weapon", "2 lesser minor rings",
        "greater minor wondrous items"
    ],
    40000: [
        "lesser medium armor", "lesser medium weapon", "lesser medium ring",
        "greater minor wondrous item", "2 greater medium potions "
    ],
    50000: [
        "greater medium armor", "greater medium weapon",
        "lesser medium wondrous item", "2 lesser major potions "
    ],
    60000: [
        "greater medium armor", "greater medium weapon",
        "2 greater minor rings", "2 greater minor wondrous items"
    ],
    75000: [
        "lesser major armor", "greater medium weapon", "greater minor ring",
        "greater medium wondrous item", "3 greater major potions "
    ],
    100000: [
        "lesser major armor", "lesser major weapon", "lesser medium ring",
        "greater minor ring", "2 lesser medium wondrous items"
    ],
}
Spellcaster_Gear = {
    1: ["4d4 sp"],
    50: ["lesser minor potion"],
    75: ["lesser minor potion", "lesser minor scroll"],
    100: ["lesser minor potion", "2 lesser minor scrolls"],
    150: ["lesser minor scroll", "greater minor scroll"],
    200: ["2 lesser minor potions", "greater minor scroll"],
    250: ["2 greater minor scrolls"],
    500: ["3 lesser minor potions", "3 greater minor scrolls"],
    750: ["greater minor potion", "lesser minor wand"],
    1000: ["3 greater minor scrolls", "lesser minor wand"],
    1500: ["lesser medium potion", "lesser medium scroll", "lesser minor wand"],
    2000: ["masterwork weapon", "2 lesser medium scrolls", "lesser minor wand"],
    2500: ["2 greater medium potions", "greater minor wand"],
    3000:
    ["greater medium potion", "2 lesser medium scrolls", "greater minor wand"],
    4000: [
        "lesser minor wondrous item", "greater medium potion",
        "greater minor wand"
    ],
    5000: [
        "lesser minor ring", "lesser minor wondrous item",
        "2 lesser medium scrolls"
    ],
    6000: [
        "lesser minor ring", "lesser minor wondrous item",
        "greater medium potion", "greater minor wand"
    ],
    7500:
    ["2 greater medium potions", "lesser minor scroll", "lesser medium wand"],
    10000:
    ["lesser minor ring", "lesser minor wondrous item", "lesser medium wand"],
    12500: [
        "lesser minor ring", "greater minor wondrous item",
        "2 greater medium scrolls", "2 greater minor wands"
    ],
    15000: ["lesser minor ring", "lesser medium rod", "lesser medium wand"],
    20000: [
        "greater minor ring", "greater minor wondrous item",
        "greater medium potion", "2 greater medium scrolls",
        "lesser medium wand"
    ],
    25000: [
        "lesser minor ring", "lesser medium wand", "greater medium wand",
        "greater minor wondrous item"
    ],
    30000: [
        "greater minor ring", "lesser medium wondrous item",
        "lesser major scroll", "greater medium wand"
    ],
    40000: [
        "lesser minor weapon", "lesser medium staff", "greater medium rod",
        "2 lesser minor wondrous items", "lesser medium wand"
    ],
    50000: [
        "greater minor ring", "2 lesser medium wondrous items",
        "lesser major potion", "3 greater medium scrolls", "lesser major wand"
    ],
    60000: [
        "lesser medium staff", "greater medium rod",
        "greater medium wondrous item", "greater medium potion",
        "2 lesser major scrolls", "lesser medium wand"
    ],
    75000: [
        "lesser minor weapon", "greater medium staff",
        "greater medium wondrous item", "3 greater major scrolls",
        "greater major wand"
    ],
    100000: [
        "lesser major ring", "greater medium rod", "lesser major staff",
        "lesser major scroll", "greater medium wand"
    ],
}
Lair_Treasure = {
    500: [
        "9d10 *3 gp", "3d8 *2 pp", "masterwork weapon", "lesser minor potion",
        "lesser minor scroll", "grade 2 gemstone"
    ],
    1000: [
        "6d8 *6 gp", "4d12 *2 pp", "greater minor potion",
        "greater minor scroll", "lesser minor wand", "3 grade 1 gemstones"
    ],
    2500: [
        "masterwork heavy armor", "masterwork weapon",
        "2 lesser medium potions", "2 greater minor scrolls"
    ],
    5000: [
        "17d8 *8 gp", "9d12 *3 pp", "masterwork weapon", "lesser minor ring",
        "greater medium potion", "lesser medium scroll", "greater minor wand"
    ],
    7500: [
        "lesser minor weapon", "lesser minor wondrous item",
        "2 greater medium potions", "greater minor wand", "2 grade 3 gemstones"
    ],
    10000: [
        "10d20 *10 gp", "9d12 *4 pp", "greater minor armor",
        "lesser minor ring", "lesser minor wondrous item",
        "lesser medium scroll", "greater minor wand", "grade 4 gemstone"
    ],
    15000: [
        "greater minor armor", "lesser minor wondrous item",
        "2 greater medium potions", "2 greater medium scrolls",
        "lesser medium wand", "1 grade 3 gemstone"
    ],
    20000: [
        "greater minor ring", "2 lesser minor wondrous items",
        "2 greater medium potions", "2 lesser major scrolls",
        "lesser medium wand"
    ],
    25000: [
        "lesser medium armor", "lesser minor weapon",
        "greater minor wondrous item", "2 lesser major scrolls",
        "lesser medium wand", "grade 4 gemstone"
    ],
    30000: [
        "greater minor weapon", "lesser medium wondrous item",
        "greater medium wand", "3 grade 3 gemstones"
    ],
    40000: [
        "lesser medium ring", "lesser medium rod", "2 greater major potions",
        "2 lesser major scrolls", "lesser major wand"
    ],
    50000: [
        "5d8 *50 gp", "8d10 *10 pp", "greater medium armor",
        "lesser medium staff", "lesser medium wondrous item",
        "greater major scroll", "lesser medium wand", "grade 5 gemstone"
    ],
    75000: [
        "greater minor weapon", "greater medium ring", "greater medium staff",
        "3 greater major potions", "greater major scroll", "lesser major wand",
        "grade 5 gemstone"
    ],
    100000: [
        "", "lesser major ring", "lesser major wondrous item",
        "3 greater major potions", "greater major scroll", "lesser medium wand",
        "2 grade 5 gemstones", "grade 6 gemstone"
    ],
}
Treasure_Horde = {
    5000: [
        "20d4 *100 cp", "12d12 *25 sp", "11d8 *10 gp", "6d6 *5 pp",
        "lesser minor armor", "greater minor wand", "5 grade 3 gemstones",
        "grade 3 art object"
    ],
    10000: [
        "11d20 *100 cp", "12d6 *50 sp", "22d8 *10 gp", "5d20 *4 pp",
        "greater minor armor", "lesser minor weapon",
        "lesser minor wondrous item", "greater medium scroll",
        "grade 4 gemstone", "grade 3 art object"
    ],
    15000: [
        "2d4 *1000 cp", "6d4 *100 sp", "3d6 *10 gp", "6d6 pp",
        "greater minor ring", "2 lesser minor wondrous items",
        "2 greater medium potions", "greater minor wand", "grade 4 gemstone",
        "grade 3 art object"
    ],
    20000: [
        "2d4 *750 cp", "6d4 *100 sp", "3d6 *40 gp", "6d6 *10 pp",
        "greater minor armor", "lesser medium rod",
        "greater minor wondrous item", "2 lesser major potions",
        "greater medium scroll", "3 grade 3 art objects"
    ],
    25000: [
        "2d4 *750 cp", "6d6 *100 sp", "18d12 *15 gp", "18d20 *4 pp",
        "lesser medium staff", "2 lesser minor wondrous items",
        "greater medium potion", "lesser medium wand", "2 grade 2 gemstones",
        "2 grade 3 gemstones", "grade 4 gemstone"
    ],
    30000: [
        "8d4 *350 cp", "7d6 *100 sp", "8d8 *30 gp", "6d12 *10 pp",
        "lesser medium armor", "greater minor weapon",
        "lesser medium wondrous item", "2 lesser major scrolls",
        "grade 4 art object"
    ],
    40000: [
        "4d4 *630 cp", "6d6 *130 sp", "2d4 *95 gp", "6d12 *11 pp",
        "lesser medium weapon", "greater medium rod", "greater major potion",
        "greater medium scroll", "lesser medium wand", "3 grade 3 art objects",
        "2 grade 4 art objects"
    ],
    50000: [
        "4d8 *450 cp", "5d20 *90 sp", "4d12 *48 gp", "7d12 *12 pp",
        "greater minor armor", "2 greater minor weapons",
        "greater medium staff", "greater minor wondrous item",
        "grade 5 gemstone"
    ],
    60000: [
        "45d100 *50 cp", "45d20 *35 sp", "4d12 *50 gp", "10d12 *10 pp",
        "greater medium weapon", "greater medium rod",
        "lesser medium wondrous item", "greater major scroll",
        "2 greater minor wands", "grade 4 gemstone", "5 grade 2 art objects"
    ],
    75000: [
        "20d20 *175 cp", "45d100 *18 sp", "4d6 *75 gp", "6d12 *15 pp",
        "lesser major armor", "greater medium ring", "lesser medium staff",
        "greater medium wand", "grade 6 gemstone", "grade 4 art object"
    ],
    100000: [
        "5d100 *190 cp", "45d100 *20 sp", "2d4 *150 gp", "4d8 *25 pp",
        "lesser medium weapon", "greater medium ring", "lesser major rod",
        "greater medium wondrous item", "2 greater major potions",
        "lesser medium scroll", "2 grade 4 art objects"
    ],
    125000: [
        "6d100 *190 cp", "50d100 *20 sp", "2d6 *150 gp", "4d10 *25 pp",
        "greater major armor", "lesser medium weapon", "lesser major staff",
        "2 greater major scrolls", "greater major wand", "grade 6 gemstone",
        "3 grade 4 art objects"
    ],
    150000: [
        "2d12 *1000 cp", "3d8 *325 sp", "4d8 *100 gp", "5d20 *18 pp",
        "greater medium armor", "lesser major ring",
        "greater major wondrous item", "greater major wand"
    ],
    200000: [
        "6d4 *1080 cp", "5d8 *300 sp", "8d4 *100 gp", "8d8 *25 pp",
        "greater major weapon", "2 lesser medium rings", "lesser major staff",
        "lesser major wondrous item", "lesser major wand",
        "3 grade 5 gemstones", "grade 4 gemstone"
    ],
    300000: [
        "4d12 *1000 cp", "8d6 *300 sp", "7d8 *100 gp", "5d12 *35 pp",
        "greater major weapon", "lesser major ring", "greater major staff",
        "greater major wondrous item", "greater medium wand",
        "grade 6 gemstone", "grade 6 art object"
    ],
}

#    1/8, 1/6, 1/4, 1/3, 1/2, 1, 2, 3, 4,    5,    6,    7,    8,    9,    10,   11,   12,   13,   14,    15,    16,
#    17,    18,    19,    20,    21,    22,    23,    24,     25,     26,     27,     28,     29,     30,     31,
Campaign_Speed_Slow = \
    [20, 30, 40, 55, 85, 170, 350, 550, 750, 1000, 1350, 1750, 2200, 2850, 3650, 4650, 6000, 7750, 10000, 13000, 16500,
     22000, 28000, 35000, 44000, 55000, 69000, 85000, 102000, 125000, 150000, 175000, 205000, 240000, 280000, 320000,
     360000, 400000, 440000, 480000, 520000, 560000, 600000, 640000, 680000, 720000, 760000, 800000, 840000, 880000,
     920000, 960000, 1000000, 1040000, 1080000, 1120000, ]
Campaign_Speed_Medium = \
    [35, 45, 65, 85, 130, 260, 550, 800, 1150, 1550, 2000, 2600, 3350, 4250, 5450, 7000, 9000, 11600, 15000, 19500,
     25000, 32000, 41000, 53000, 67000, 84000, 104000, 127000, 155000, 185000, 220000, 260000, 305000, 360000, 420000,
     480000, 540000, 600000, 660000, 720000, 780000, 840000, 900000, 960000, 1020000, 1080000, 1140000, 1200000,
     1260000, 1320000, 1380000, 1440000, 1500000, 1560000, 1620000, 1680000, ]
Campaign_Speed_Fast = \
    [50, 65, 100, 135, 200, 400, 800, 1200, 1700, 2300, 3000, 3900, 5000, 6400, 8200, 10500, 13500, 17500, 22000, 29000,
     38000, 48000, 62000, 79000, 100000, 125000, 155000, 190000, 230000, 275000, 330000, 390000, 460000, 540000, 630000,
     720000, 810000, 900000, 990000, 1080000, 1170000, 1260000, 1350000, 1440000, 1530000, 1620000, 1710000, 1800000,
     1890000, 1980000, 2070000, 2160000, 2250000, 2340000, 2430000, 2520000, ]

Campaign_Speed = Campaign_Speed_Medium


def treasure_calculator(treasure, species, cr):
    if species not in list(Monster_Types.keys()):
        return None
    all_items = []
    additional = ''
    mult = 0
    match = re.match(r'NPG gear \((.*)\)', treasure)
    if match is not None:
        # Add some gold with whatever is in group 1
        additional = match.group(1)
    else:
        match = re.match(r'([ \w])+ \((.*)\)', treasure)
        if match is not None:
            additional = match.group(2)
            treasure = match.group(1)

    # Basic Cases
    if treasure == 'standard':
        mult = 1
    elif treasure == 'half standard':
        mult = 0.5
    elif treasure == 'double standard':
        mult = 2
    elif treasure == 'triple standard':
        mult = 3

    if float(cr) == .13:
        budget = Campaign_Speed[0]
    elif float(cr) == .17:
        budget = Campaign_Speed[1]
    elif float(cr) == .25:
        budget = Campaign_Speed[2]
    elif float(cr) == .33:
        budget = Campaign_Speed[3]
    elif float(cr) == .5:
        budget = Campaign_Speed[4]
    else:
        budget = Campaign_Speed[int(float(cr)) + 4]

    all_items += treasure_samples(mult, Monster_Types[species], budget)

    totalMoney = 0
    i = 0
    while i < len(all_items):
        if isinstance(all_items[i], int) or isinstance(all_items[i], float):
            totalMoney += all_items[i]
            all_items.pop(i)
        else:
            # all_items[i] = all_items[i].to_string()
            i += 1

    if additional != '':
        for item in additional.split(','):
            s = '<tr><td style="width:50%;"><span class="text-md">' + item.strip() + '</span></td><td> --- ' + \
                '</td><td>Common</td></tr>'
            all_items.append(s)
    s = '<tr><td style="width:50%;"><span class="text-md">Spare Change</span></td><td>' + determine_cost(totalMoney) + \
        '</td><td>Common</td></tr>'
    all_items.append(s)
    return all_items


def treasure_samples(quantity, item_groups, budget):
    all_items = []
    while budget > 0:
        category = choose_treause(choice(item_groups))
        available = []
        for item in list(category.keys()):
            if item <= budget:
                available.append(item)
        if not available:
            continue
        item_key = choice(available)
        budget -= item_key
        for items in category[item_key]:
            func = determine_treasure(items)
            if func is not None:
                ret = func(items)
                if isinstance(ret, float) or isinstance(ret, int):
                    all_items.append(ret)
                else:
                    all_items += ret
    return all_items


def choose_treause(item):
    if item == 'Coins':
        return Coins
    elif item == 'Coins and Gems':
        return Coins_and_Gems
    elif item == 'Art Objects':
        return Art_Objects
    elif item == 'Coins & Small Objects':
        return Coins_and_Objects
    elif item == 'Armor and weapons':
        return Armor_and_Weapons
    elif item == 'Combatant Gear':
        return Combatant_Gear
    elif item == 'Spellcaster Gear':
        return Spellcaster_Gear
    elif item == 'Lair Treasure':
        return Lair_Treasure
    elif item == 'Treasure Horde':
        return Treasure_Horde
    else:
        return None


def determine_treasure(s):
    if s.strip().split(' ')[-1] == 'scroll' or s.strip().split(
            ' ')[-1] == 'scrolls':
        return scroll
    elif s.strip().split(' ')[-1] == 'ring' or s.strip().split(
            ' ')[-1] == 'rings':
        return ring
    elif s.strip().split(' ')[-1] == 'pp' or s.strip().split(' ')[-1] == 'gp' or \
            s.strip().split(' ')[-1] == 'sp' or s.strip().split(' ')[-1] == 'cp':
        return money
    elif s.strip().split(' ')[-1] == 'gemstone' or s.strip().split(
            ' ')[-1] == 'gemstones':
        return gemstone
    elif s.strip().split(' ')[-1] == 'weapon' or s.strip().split(
            ' ')[-1] == 'weapons':
        return weapon
    elif s.strip().split(' ')[-1] == 'armor' or s.strip().split(
            ' ')[-1] == 'armors':
        return armor
    elif s.strip().split(' ')[-1] == 'scroll' or s.strip().split(
            ' ')[-1] == 'scrolls':
        return scroll
    elif s.strip().split(' ')[-1] == 'wand' or s.strip().split(' ')[-1] == 'wands' or \
            s.strip().split(' ')[-1] == 'rod' or s.strip().split(' ')[-1] == 'rods' or \
            s.strip().split(' ')[-1] == 'staff' or s.strip().split(' ')[-1] == 'staffs':
        return wand
    elif s.strip().split(' ')[-1] == 'potion' or s.strip().split(
            ' ')[-1] == 'potions':
        return potion
    elif s.strip().split(' ')[-1] == 'object' or s.strip().split(
            ' ')[-1] == 'objects':
        return art
    elif s.strip().split(' ')[-1] == 'item' or s.strip().split(
            ' ')[-1] == 'items':
        return wondrous
    else:
        return None


def potion(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    category = ''
    quantity = 0
    for p in primary:
        if category != '':
            break
        for s in secondary:
            match = re.match(
                re.compile('([\d ]*)' + p + ' ' + s + ' potion[s]?'), g)
            if match is not None:
                if match.group(1) == '' or match.group(1) is None:
                    quantity = 1
                else:
                    quantity = int(match.group(1))
                category = (p, s)
                break

    for _ in range(quantity):
        if category[1] == 'minor':
            l.append(Potion(randint(0, 3)))
        elif category[1] == 'medium':
            l.append(Potion(randint(2, 5)))
        elif category[1] == 'major':
            l.append(Potion(randint(4, 9)))
    return l


def armor(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    category = ''
    quantity = 0
    if 'masterwork' in g:
        f = g.split(' ')
        a = Armor(randint(0, 4), iClass=f[1].title())
        a.add_masterwork(randint(0, 9))
        l.append(a)
    else:
        for p in primary:
            if category != '':
                break
            for s in secondary:
                match = re.match(
                    re.compile('([\d ]*)' + p + ' ' + s + ' armor[s]?'), g)
                if match is not None:
                    if match.group(1) == '' or match.group(1) is None:
                        quantity = 1
                    else:
                        quantity = int(match.group(1))
                    category = (p, s)
                    break

        for _ in range(quantity):
            if category[1] == 'minor':
                l.append(Armor(randint(0, 1)))
            elif category[1] == 'medium':
                l.append(Armor(randint(1, 2)))
            elif category[1] == 'major':
                l.append(Armor(randint(3, 4)))
    return l


def weapon(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    category = ''
    quantity = 0
    if 'masterwork' in g:
        w = Weapon(randint(0, 4))
        w.add_masterwork(randint(0, 9))
        l.append(w)
    else:
        for p in primary:
            if category != '':
                break
            for s in secondary:
                match = re.match(
                    re.compile('([\d ]*)' + p + ' ' + s + ' weapon[s]?'), g)
                if match is not None:
                    if match.group(1) == '' or match.group(1) is None:
                        quantity = 1
                    else:
                        quantity = int(match.group(1))
                    category = (p, s)
                    break

        for _ in range(quantity):
            if category[1] == 'minor':
                w = Weapon(randint(0, 1))
            elif category[1] == 'medium':
                w = Weapon(randint(1, 2))
            elif category[1] == 'major':
                w = Weapon(randint(3, 4))
            else:
                w = Weapon(0)
            l.append(w)
    return l


def wondrous(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    quantity = 0
    category = ''
    for p in primary:
        if category != '':
            break
        for s in secondary:
            match = re.match(
                re.compile('([\d ]*)' + p + ' ' + s + ' wondrous item[s]?'), g)
            if match is not None:
                if match.group(1) == '' or match.group(1) is None:
                    quantity = 1
                else:
                    quantity = int(match.group(1).strip())
                category = (p, s)
                break

    for _ in range(quantity):
        if category[0] == 'lesser' and category[1] == 'minor':
            l.append(Wondrous(randint(1, 3)))
        elif category[0] == 'lesser' and category[1] == 'medium':
            l.append(Wondrous(randint(2, 6)))
        elif category[0] == 'lesser' and category[1] == 'major':
            l.append(Wondrous(randint(4, 9)))
        if category[0] == 'greater' and category[1] == 'minor':
            l.append(Wondrous(randint(8, 13)))
        elif category[0] == 'greater' and category[1] == 'medium':
            l.append(Wondrous(randint(12, 16)))
        elif category[0] == 'greater' and category[1] == 'major':
            l.append(Wondrous(choice([16, 17, 18, 19, 20, 22])))
    return l


def art(s):
    l = []
    match = re.match(r'([\d ]*)grade (\d) art object[s]?', s)
    if match.group(1) is None or match.group(1) == '':
        l.append(Art(int(match.group(2)) - 1))
    else:
        for _ in range(int(match.group(1))):
            l.append(Art(int(match.group(2)) - 1))
    return l


def ring(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    category = ''
    quantity = 0
    for p in primary:
        if category != '':
            break
        for s in secondary:
            match = re.match(
                re.compile('([\d ]*)' + p + ' ' + s + ' ring[s]?'), g)
            if match is not None:
                if match.group(1) == '' or match.group(1) == None:
                    quantity = 1
                else:
                    quantity = int(match.group(1))
                category = (p, s)
                break

    for _ in range(quantity):
        if category[1] == 'minor':
            l.append(Ring(randint(0, 3)))
        elif category[1] == 'medium':
            l.append(Ring(randint(2, 5)))
        elif category[1] == 'major':
            l.append(Ring(randint(4, 9)))
    return l


def wand(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    category = ''
    quantity = 0
    for p in primary:
        if category != '':
            break
        for s in secondary:
            match = re.match(
                re.compile('([\d ]*)' + p + ' ' + s + ' wand[s]?'), g)
            if match is not None:
                if match.group(1) == '' or match.group(1) == None:
                    quantity = 1
                else:
                    quantity = int(match.group(1))
                category = (p, s)
                break

    for _ in range(quantity):
        if category[1] == 'minor':
            l.append(Scroll(randint(0, 3)))
        elif category[1] == 'medium':
            l.append(Scroll(randint(2, 5)))
        elif category[1] == 'major':
            l.append(Scroll(randint(4, 9)))
    return l


def gemstone(g):
    l = []
    match = re.match(r'([\d ]*)grade (\d) gemstone[s]?', g)
    if match.group(1) == '':
        l.append(Jewel(int(match.group(2)) - 1))
    else:
        for _ in range(int(match.group(1).strip())):
            l.append(Jewel(int(match.group(2)) - 1))
    return l


def money(s):
    match = re.match(r'(\d+)d(\d+) ([csgp]p)', s)
    if match is not None:
        # No need to multiply
        m = sum(randint(1, int(match.group(2)) + 1, size=int(match.group(1))))
        if not isinstance(m, int):
            m = int(m)
        if match.group(3) == 'cp':
            m *= .01
        elif match.group(3) == 'sp':
            m *= .1
        elif match.group(3) == 'pp':
            m *= 10

    match = re.match(r'(\d+)d(\d+) \*(\d+) ([csgp]p)', s)
    if match is not None:
        # Multiply
        m = sum(randint(1, int(match.group(2)) + 1, size=int(
            match.group(1)))) * int(match.group(3))
        if not isinstance(m, int):
            m = int(m)
        if match.group(4) == 'cp':
            m *= .01
        elif match.group(4) == 'sp':
            m *= .1
        elif match.group(4) == 'pp':
            m *= 10
        m *= int(match.group(3))
    return round(m, 2)


def scroll(g):
    l = []
    primary = ['lesser', 'greater']
    secondary = ['minor', 'medium', 'major']
    category = ''
    quantity = 0
    for p in primary:
        for s in secondary:
            match = re.match(re.compile('([\d ])*' + p + ' ' + s + ' [\d]+'), g)
            if match is not None:
                quantity = int(match.group(1).strip())
                category = (p, s)
                break
    for _ in range(quantity):
        if category[1] == 'minor':
            l.append(Scroll(randint(0, 1)))
        elif category[1] == 'medium':
            l.append(Scroll(randint(1, 2)))
        elif category[1] == 'major':
            l.append(Scroll(randint(3, 4)))
    return l


def print_treasure(monster_name='', monster_cr=0.0):
    import os
    from bs4 import BeautifulSoup as bs
    import simplejson as json

    with open("generate.json", 'r') as inf:
        settings = json.load(inf)

    Beasts = {}
    with open('beasts.json', 'r') as inf:
        Beasts.update(json.load(inf, encoding='utf-8'))
    if settings["Allow Pokemon"]:
        with open('pokemon.json', 'r') as inf:
            Beasts.update(json.load(inf, encoding='utf-8'))

    if 'beasts' not in os.listdir(os.getcwd()):
        try:
            os.mkdir(os.getcwd() + '/beasts')
        except OSError:
            print("Beasts directory creation failed")
    if monster_name not in list(Beasts.keys()) and monster_cr == 0.0:
        # Choose a random monster
        monster_name = choice(list(Beasts.keys()))
        monster = Beasts[monster_name]
    elif monster_cr in [
            '0.13', '0.17', '0.25', '0.33', '0.5', '1.0', '2.0', '3.0', '4.0',
            '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0',
            '14.0', '15.0', '16.0', '17.0', '18.0', '19.0', '20.0', '21.0',
            '22.0', '23.0', '24.0', '25.0', '26.0', '27.0', '28.0', '29.0',
            '30.0', '35.0', '37.0', '39.0'
    ]:
        # Choose a monster based on CR
        monster_name = choice(list(Beasts.keys()))
        monster = Beasts[monster_name]
        while monster['CR'] != monster_cr:
            monster_name = choice(list(Beasts.keys()))
            monster = Beasts[monster_name]
    else:
        monster = Beasts[monster_name]

    html = '<!DOCTYPE html><html><head><meta content="width=device-width" name="viewport"/><title></title><style>' + \
           'body {max-width:800px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px;} html' + \
           '{font-family:Arial;}h1, h2 {color:black;text-align:center;} .center{text-align:center;} .bold' + \
           '{font-weight:bold;}.emp{font-style:italic;} table{border:1px solid black;border-spacing:0px;}' + \
           'table tr th {background-color:gray;color:white;padding:5px;}table tr td {margin:0px;padding:5px;}' + \
           '.text-xs{font-size:12px;}.text-sm{font-size:14px;}.text-md{font-size:18px;}.text-lg{font-size:24px;}' + \
           '.text-xl{font-size:32px;}.col-1-3{width:33.3%;float: left;}.col-2-3{width:50%;float:left;}' + \
           '.col-3-3{width:100%;float:left;}.col-1-2{width:50%;float:left;}.col-2-2{width:100%;float:left;}' + \
           '.col-1-4{width:25%;float:left;}.col-2-4{width:33.3%;float:left;}.col-3-4{width:50%;float:left;}' + \
           '.col-4-4{width:100%;float:left;}</style><style type="text/css">.inventory-table td{border-bottom:' + \
           '1px solid black;}.wrapper-box{width:100%;border:2px solid black;padding:5px;}</style></head>' + \
           '<script>function show_hide(ident){\nvar a = document.getElementById(ident);\nif (a.style.display ===' + \
           "'none'){\na.style.display = 'block';} else {a.style.display = 'none';}}</script>" + \
           '<body><h1 style="text-align: center;">' + monster_name + ' Treasure</h1><table class="inventory-table" ' + \
           'style="width:100%;"><tbody><tr><th style="text-align:left;">Item</th><th style="text-align:left;">' + \
           'Cost</th><th style="text-align:left;">Rarity</th></tr>'

    treasure = treasure_calculator(monster['Treasure'], monster['Type'],
                                   monster['CR'])
    for t in treasure:
        html += str(t)
    html += '</tr></table></body></html>'
    with open('beasts/' + monster_name + ' Treasure.html', 'w') as outf:
        outf.write(bs(html, 'html5lib').prettify())


if __name__ == '__main__':
    monster_name = ''
    monster_cr = '7.0'
    print_treasure(monster_name, monster_cr)
