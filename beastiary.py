#!!usr/bin/python3

from bs4 import BeautifulSoup as bs
from numpy.random import choice
from treasure import treasure_calculator
import re
from tqdm import tqdm
from numpy.random import randint
import os
import simplejson as json

with open("generate.json", 'r') as inf:
    settings = json.load(inf)

Beasts = {}
with open('beasts.json', 'r') as inf:
    Beasts.update(json.load(inf, encoding='utf-8'))
if settings["Allow Pokemon"]:
    with open('pokemon.json', 'r') as inf:
        Beasts.update(json.load(inf, encoding='utf-8'))
    with open('pokemon_moves.json', 'r') as inf:
        Poke_moves = json.load(inf, encoding='utf-8')

Levels = {
    '0.13': 50,
    '0.17': 65,
    '0.25': 100,
    '0.33': 135,
    '0.5': 200,
    '1.0': 400,
    '2.0': 600,
    '3.0': 800,
    '4.0': 1200,
    '5.0': 1600,
    '6.0': 2400,
    '7.0': 3200,
    '8.0': 4800,
    '9.0': 6400,
    '10.0': 9600,
    '11.0': 12800,
    '12.0': 19200,
    '13.0': 25600,
    '14.0': 38400,
    '15.0': 51200,
    '16.0': 76800,
    '17.0': 102400,
    '18.0': 153600,
    '19.0': 204800,
    '20.0': 307200,
    '21.0': 409600,
    '22.0': 615000,
    '23.0': 820000,
    '24.0': 1230000,
    '25.0': 1640000,
    '26.0': 2457600,
    '27.0': 3276800,
    '28.0': 4915200,
    '29.0': 6553600,
    '30.0': 9830400,
    '35.0': 52480000,
    '37.0': 104960000,
    '39.0': 209920000,
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


def roll_hp(string):
    if '+' in string:
        m = re.match(r'(\d+)d(\d+)\+(\d+)', string)
    elif '-' in string:
        m = re.match(r'(\d+)d(\d+)(\-\d+)', string)
    else:
        m = re.match(r'(\d+)d(\d+)', string)
    total = 0
    for _ in range(int(m.group(1))):
        total += randint(int(m.group(2))) + 1
    if len(m.groups()) == 3:
        total += int(m.group(3))
    return str(total)


def pokemon_moves(name='', tm=0):
    html = '<table><td style="width: 50%"><span class="text-md">'
    # weapon[1] + ' (' + weapon[2] + ')</span></td></table><br/>'
    if name == '' and tm == 0:
        return None
    elif tm == 0:
        try:
            move = Poke_moves[name]
            html += '<a href"' + move['link'] + '">' + name.title() + '</a>(PP: ' + str(move['pp']) + ')<i>' + \
                    move['type'] + '</i>/span><br /><span class="text-sm emp">' + move['school'] + ' | ' + move['range']
        except KeyError:
            return None
    else:
        pass
    return html


def get_monster_type(dictionary):
    if "Pokedex" in list(dictionary.keys()):
        return 'Pokemon'
    else:
        return 'Pathfinder'


def print_monster(picked_monster):
    if 'beasts' not in os.listdir(os.getcwd()):
        try:
            os.mkdir(os.getcwd() + '/beasts')
        except OSError:
            print("Beasts directory creation failed")

    name = picked_monster[0]
    monster = picked_monster[1]
    monster_type = get_monster_type(monster)

    abilities = re.match(
        r'Str\s+([\d\-]*),\s+Dex\s+([\d\-]*),\s+Con\s+([\d\-]*),\s+Int\s+([\d\-]*),\s+Wis\s+([\d\-]*),\s+Cha\s+([\d\-]*)',
        monster['AbilityScores'])

    if monster_type == 'Pokemon':
        armor = monster['AC']
        saves = None
    else:
        armor = re.match(r'(\-?\d+), touch (\-?\d+), flat-footed (\-?\d+)', monster['AC'])
        saves = re.match(r'Fort ([+-]\d+[\S ]*), Ref ([+-]\d+[\S ]*), Will ([+-]\d+[\S ]*)', monster['Saves'])

    # Base HTML
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
           name + '</span>-<span class="text-md bold">CR ' + str(monster['CR']) + '</span>&emsp;<span>(EXP: '

    html += str(Levels[str(float(monster['CR']))]) + ')</span><p>'
    for line in monster['Description'].split('.'):
        html += '<p>' + line + '</p>'

    # Add basic Stats
    if monster_type == 'Pathfinder':
        html += '<div><ul style="column-count: 2; list-style-type: none;margin: 5px"><li style="padding-top: 6px;' + \
                'padding-bottom: 6px;"><span style="font-weight:bold;">HP:</span>' + roll_hp(monster['HD']) + ' (' + \
                monster['HD'] + ')</li><li style="padding-top: 6px;padding-bottom: 6px;"><span style="font-weight:' + \
                'bold;">Speed:</span>' + monster['Speed'] + '</li><li style="padding-top: 6px;padding-bottom: 6px;">' + \
                '<span style="font-weight:bold;">Size:</span>' + monster['Size'] + '</li><li><table><th>AC:</th><td>' + \
                armor.group(1) + '</td><th>Touch:</th><td>' + armor.group(2) + '</td><th>Flat:</th><td>' + armor.group(3) +\
                '</td></table></li><li><table><th>Attack:' + '</th><td>' + monster['BaseAtk'] + '</td><th>CMB:</th><td>' + \
                monster['CMB'] + '</td><th>CMD:</th><td>' + monster['CMD'] + '</td></table></li>'
        if saves is not None:
            html += '<li><table><th>Fort:</th><td>' + saves.group(1) + '</td><th>Ref:</th><td>' + saves.group(2) + \
                '</td><th>Will:</th><td>' + saves.group(3) + '</td></table></li>'
    elif monster_type == 'Pokemon':
        html += '<div><ul style="column-count: 2; list-style-type: none;margin: 5px"><li style="padding-top: 6px;' + \
                'padding-bottom: 6px;"><span style="font-weight:bold;">HP:</span>' + roll_hp(monster['HD']) + ' (' + \
                monster['HD'] + ')</li><li style="padding-top: 6px;padding-bottom: 6px;"><span style="font-weight:' + \
                'bold;">Speed:</span>' + monster['Speed'] + '</li><li style="padding-top: 6px;padding-bottom: 6px;">' + \
                '<span style="font-weight:bold;">Size:</span>' + monster['Size'] + '</li>'

    # Add Base Stats
    html += '</ul></div><table class="inventory-table"style="width: 100%;"><tr><th>STR</th><th>DEX</th><th>CON</th>' + \
            '<th>INT</th><th>WIS</th><th>CHA</th></tr><tr>'

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
    if monster_type == 'Pokemon':
        # print('Pokemon Moves')
        for move in monster['Moves']['Start']:
            move_info = Poke_moves[move]
            html += '<table><td style="width: 50%"><span class="text-md"><a href="' + move_info['link'] + '">' + \
                    move + '</a> <i>(PP: ' + str(move_info['pp']) + ')</i></span><br /><span class="text-sm emp">' + \
                    '<b>Type:</b>' + move_info['type'] + '<b>Time:</b> ' + move_info['casting_time'] + \
                    '<b>Range:</b> ' + move_info['range'] + '</span>' + move_info['description'] + '</td></table><br/>'
    else:
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

    if monster_type == 'Pokemon':
        treasure = treasure_calculator(monster['Treasure'], "humanoid", monster['CR'])
    else:
        treasure = treasure_calculator(monster['Treasure'], monster['Type'], monster['CR'])
    for t in treasure:
        html += str(t)
    html += '</tr></table></body></html>'
    with open('beasts/' + name + '.html', 'w') as outf:
        outf.write(bs(html, 'html5lib').prettify())


if __name__ == '__main__':
    import time
    import shutil

    print('########################')
    print('# Running all monsters #')
    print('########################')
    print()

    if 'beasts' not in os.listdir(os.getcwd()):
        try:
            shutil.rmtree('beasts')
            os.mkdir(os.getcwd() + '/beasts')
        except OSError:
            print("Beasts directory creation failed")

    time.sleep(.1)

    for m in tqdm(list(sorted(Beasts.keys()))):
        print_monster(pick_monster(name=m))
