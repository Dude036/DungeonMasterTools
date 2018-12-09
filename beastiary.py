#!!usr/bin/python3

from bs4 import BeautifulSoup as bs
from numpy.random import choice
from treasure import treasure_calculator
import time
from yapf.yapflib.yapf_api import FormatFile, FormatCode
import re
from tqdm import tqdm
from beast_list import Beasts
import os

Levels = {
    '0.13': 50,
    '0.17': 65,
    '0.25': 100,
    '0.33': 135,
    '0.50': 200,
    '1.00': 400,
    '2.00': 600,
    '3.00': 800,
    '4.00': 1200,
    '5.00': 1600,
    '6.00': 2400,
    '7.00': 3200,
    '8.00': 4800,
    '9.00': 6400,
    '10.00': 9600,
    '11.00': 12800,
    '12.00': 19200,
    '13.00': 25600,
    '14.00': 38400,
    '15.00': 51200,
    '16.00': 76800,
    '17.00': 102400,
    '18.00': 153600,
    '19.00': 204800,
    '20.00': 307200,
    '21.00': 409600,
    '22.00': 615000,
    '23.00': 820000,
    '24.00': 1230000,
    '25.00': 1640000,
    '26.00': 2457600,
    '27.00': 3276800,
    '28.00': 4915200,
    '29.00': 6553600,
    '30.00': 9830400,
    '35.00': 52480000,
    '37.00': 104960000,
    '39.00': 209920000,
}
index = 0


def pick_monster(name='', cr=-1.0):
    monster = None
    if name == '':
        # Pick a random Monster.
        if cr == -1.0:
            cr = choice(list(Levels.keys()))
        name = choice(list(Beasts.keys()))
        monster = Beasts[name]
        # print(monster['CR'])
        while monster['CR'] != cr:
            name = choice(list(Beasts.keys()))
            monster = Beasts[name]
            # print(monster['CR'])

    elif name in list(Beasts.keys()):
        # Check if Monster is in the Dictionary, if not, it'll return None
        monster = Beasts[name]
    return name, monster


def print_monster(picked_monster):
    if 'beasts' not in os.listdir(os.getcwd()):
        try:
            os.mkdir(os.getcwd() + '/beasts')
        except OSError:
            print("Beasts directory creation failed")

    name = picked_monster[0]
    monster = picked_monster[1]

    abilities = re.match(
        r'Str\s+([\d\-]*),\s+Dex\s+([\d\-]*),\s+Con\s+([\d\-]*),\s+Int\s+([\d\-]*),\s+Wis\s+([\d\-]*),\s+Cha\s+([\d\-]*)',
        monster['AbilitiyScores'])
    armor = re.match(r'(\-?\d+), touch (\-?\d+), flat-footed (\-?\d+)',
                     monster['AC'])
    saves = re.match(
        r'Fort ([+-]\d+[\S ]*), Ref ([+-]\d+[\S ]*), Will ([+-]\d+[\S ]*)',
        monster['Saves'])
    # -5 + int(n / 2)
    if saves is None or armor is None or abilities is None:
        print(name)
        print('\tS:\t', saves)
        print('\tR:\t', armor)
        print('\tA:\t', abilities)

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
           """""""'none'){\na.style.display = 'block';} else {a.style.display = 'none';}}</script>""" + \
           '<body><table class="wrapper-box" style="margin-bottom:60px;"><tr><td><span class="text-lg bold">' + \
           name + '</span>-<span class="text-md bold">CR ' + monster['CR'] + '</span>&emsp;<span>(EXP: ' + \
           str(format(Levels[monster['CR']], ',d')) + ')</span><p>'
    for line in monster['Description'].split('.'):
        html += '<p>' + line + '</p>'
    html += '<div><ul style="column-count: 2; list-style-type: none;margin: 5px"><li style="padding-top: 6px;' + \
            'padding-bottom: 6px;"><span style="font-weight:bold;">HP:</span>' + monster['HP'] + ' ' + monster['HD'] + \
            '</li><li style="padding-top: 6px;padding-bottom: 6px;"><span style="font-weight:bold;">Speed:</span>' + \
            monster['Speed'] + '</li><li style="padding-top: 6px;padding-bottom: 6px;"><span style="font-weight:bold' +\
            ';">Size:</span>' + monster['Size'] + '</li><li><table><th>AC:</th><td>' + armor.group(1) + \
            '</td><th>Touch:</th><td>' + armor.group(2) + '</td><th>Flat:</th><td>' + armor.group(3) + \
            '</td></table></li><li><table><th>Attack:' + '</th><td>' + monster['BaseAtk'] + '</td><th>CMB:</th><td>' + \
            monster['CMB'] + '</td><th>CMD:</th><td>' + monster['CMD'] + '</td></table></li><li><table><th>Fort:' + \
            '</th><td>' + saves.group(1) + '</td><th>Ref:</th><td>' + saves.group(2) + '</td><th>Will:</th><td>' + \
            saves.group(3) + '</td></table></li></ul></div><table class="inventory-table" style="width: 100%;">' + \
            '<tr><th>STR</th><th>DEX</th><th>CON</th><th>INT</th><th>WIS</th><th>CHA</th></tr><tr>'

    for a in range(6):
        if abilities is None:
            print(name)
        if abilities.group(a + 1) == '-':
            add = '- (-)'
        else:
            b = -5 + int(int(abilities.group(a + 1)) / 2)
            if b >= 0:
                add = '+' + str(b)
            else:
                add = str(b)
        html += '<td style = "text-align: center;">' + str(
            abilities.group(a + 1)) + ' (' + add + ')</td>'
    html += '</tr></table><ul style="columns: 2;padding: 10px;">'

    total_weapons = 0

    if monster['Melee'] != '':
        all_weapons = re.findall(
            r'(\d{0,3}\s*[\w ]+)[\s]+([\+\-\d\/]+)[\s]+\(([\w\d\-\+\\\/\.\,\'\; ]+)\)',
            monster['Melee'])
        if all_weapons:
            for weapon in all_weapons:
                html += '<table><td style="width: 50%"><span class="text-md">' + weapon[0].strip().title() + \
                        '</span><br /><span class="text-sm emp">' + weapon[1] + ' (' + weapon[2] + \
                        ')</span></td></table><br/>'
                total_weapons += 1
        else:
            print(name, '\t', monster['Melee'])

    if monster['Ranged'] != '':
        all_weapons = re.findall(
            r'(\d{0,3}\s*[\w ]+)[\s]+([\+\-\d\/]+)[\s]+\(([\w\d\-\+\\\/\.\,\'\; ]+)\)',
            monster['Ranged'])
        if all_weapons:
            for weapon in all_weapons:
                html += '<table><td style="width: 50%"><span class="text-md">' + weapon[0].strip().title() + \
                        '</span><br /><span class="text-sm emp">' + weapon[1] + ' (' + weapon[2] \
                        + ')</span></td></table>' + '<br/>'
                total_weapons += 1
        else:
            print(name, '\t', monster['Ranged'])

    if total_weapons % 2 == 1:
        html += '<table><td style="width: 50%"><span class="text-md"></span><br /><span class="text-sm emp"></span>' + \
                '</td></table>'
    html += '</ul><p><strong>Treasure:</strong></p><table class="inventory-table" style="width:100%;"><tbody><tr>' + \
            '<th style="text-align:left;">Item</th><th style="text-align:left;">Cost</th><th style="text-align:left;">' + \
            'Rarity</th></tr>'
    treasure = treasure_calculator(monster['Treasure'], monster['Type'],
                                   monster['CR'])
    for t in treasure:
        html += str(t)
    html += '</tr></table></body></html>'
    with open('beasts/' + name + '.html', 'w') as outf:
        outf.write(bs(html, 'html5lib').prettify())


def print_treasure(picked_monster):
    if 'beasts' not in os.listdir(os.getcwd()):
        try:
            os.mkdir(os.getcwd() + '/beasts')
        except OSError:
            print("Beasts directory creation failed")

    name = picked_monster[0]
    monster = picked_monster[1]

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
           '<body><table class="inventory-table" style="width:100%;"><tbody><tr><th style="text-align:left;">Item'\
           '</th><th style="text-align:left;">Cost</th><th style="text-align:left;">Rarity</th></tr>'

    treasure = treasure_calculator(monster['Treasure'], monster['Type'],
                                   monster['CR'])
    for t in treasure:
        html += str(t)
    html += '</tr></table></body></html>'
    with open('beasts/' + name + ' Treasure.html', 'w') as outf:
        outf.write(bs(html, 'html5lib').prettify())


def add_to_beastiary(dict_name, dict_keys):
    Beasts[dict_name] = dict_keys
    open('beast_list.py', 'w').write(FormatCode(str(Beasts)))


if __name__ == '__main__':
    print('########################')
    print('# Running all monsters #')
    print('########################')
    print()

    if 'beasts' not in os.listdir(os.getcwd()):
        try:
            os.mkdir(os.getcwd() + '/beasts')
        except OSError:
            print("Beasts directory creation failed")

    time.sleep(.1)

    for m in tqdm(list(sorted(Beasts.keys()))):
        print_monster(pick_monster(name=m))
