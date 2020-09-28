import simplejson as json
from pprint import pprint
import re


def mk_to_html(line):
    done = False
    # Only once
    while not done:
        done = True
        # line = line.replace('>', '')
        if '#####' in line:
            line = re.sub(r'#####', '', line).strip()
            line = '<h4>' + line + '</h4>'
        elif '####' in line:
            line = re.sub(r'####', '', line).strip()
            line = '<h3>' + line + '</h3>'
        elif '###' in line:
            line = re.sub(r'###', '', line).strip()
            line = '<h2>' + line + '</h2>'
        elif '##' in line:
            line = re.sub(r'##', '', line).strip()
            line = '<h1>' + line + '</h1>'
        elif '___' in line:
            line = '<hr>'

        # Multi options
        if '***' in line:
            done = False
            while '***' in line:
                line = re.sub(r'\*\*\*', '<b><i>', line)
                line = re.sub(r'\*\*\*', '</b></i>', line)
        if '**' in line:
            done = False
            while '**' in line:
                line = re.sub(r'\*\*', '<b>', line)
                line = re.sub(r'\*\*', '</b>', line)
        if '*' in line:
            done = False
            while '*' in line:
                line = re.sub(r'\*', '<i>', line)
                line = re.sub(r'\*', '</i>', line)

    return line

def mk_table(lines):
    html = '<table>'
    first_line = False
    for line in lines:
        html += '<tr>'
        for cell in line.split('|'):
            if cell != '' and cell != '>':
                html += '<td>' + cell + '</td>'
                
        html += '</tr>'
    html += '</table>'
    return html

links = json.load(open("5e_links.json", 'r', encoding='utf-8'))

creatures = {}

all_lines = ''
with open('bestiary.md', 'r', encoding='utf-8') as inf:
    all_lines = inf.read()

all_monsters = all_lines.split('>## ')

for monster in all_monsters[1:]:
    # Parsed Info
    lines = monster.split('\n')
    name = lines[0].strip()
    print(name)
    link = links[lines[0].strip()]
    size = lines[1].split(' ')[0][2:]
    c_type = ' '.join(lines[1].split(',')[0][2:].split(' ')[1:])
    if 'humanoid' in c_type:
        c_type = 'humanoid'
    alignment = lines[1][lines[1].rindex(','):-1]
    if alignment.lower() == 'unaligned':
        align = alignment
    elif alignment.lower() == 'neutral':
        align = 'N'
    else:
        align = alignment.split(' ')[0][0].upper() + alignment.split(' ')[1][0].upper()

    AC = lines[3][19:21].strip()
    hit_dice = re.match(r'.*\((.*)\)', lines[4])
    if hit_dice is not None:
        HD = hit_dice.group(1)
    else:
        HD = lines[4][18:]
    speed = lines[5][13:]

    stats = re.findall(r'\|(\d+)', lines[9])
    STR, DEX, CON, INT, WIS, CHA = stats

    current = 11
    saves = skills = lang = resist = immune = weak = CR = XP = None
    while '>___' not in lines[current]:
        if '**Saving Throws**' in lines[current]:
            saves = lines[current][21:]
        elif '**Skills**' in lines[current] or '**Senses**' in lines[current]:
            skills = lines[current][14:] + ', '
        elif '**Languages**' in lines[current]:
            lang = lines[current][17:]
        elif '**Damage Resistances**' in lines[current]:
            resist = lines[current][26:] + ', '
        elif '**Condition Resistances**' in lines[current]:
            resist = lines[current][28:] + ', '
        elif '**Damage Immunities**' in lines[current]:
            immune = lines[current][25:]
        elif '**Damage Vulnerabilities**' in lines[current]:
            weak = lines[current][30:]
        elif '**Challenge**' in lines[current]:
            if lines[current][17:].split(' ')[0] == '-':
                CR = '0.0'
                XP = '0'
            else:
                CR = str(float(eval(lines[current][17:].split(' ')[0])))
                XP = lines[current][17:].split(' ')[1][1:]
                XP = XP.replace(',', '')

        current += 1

    # Feats
    feats = ''
    while '>### Actions' not in lines[current]:
        if '>***' in lines[current]:
            t_feat = lines[current][4:]
            feats += mk_to_html(t_feat) + '<br>'
        current += 1

    current += 1
    # Actions
    melee = ''
    while '>' in lines[current]:
        if 'Multiattack' in lines[current]:
            pass
        elif len(lines[current]) <= 1:
            pass
        else:
            dice_name = lines[current].split('***')
            cont_text = ''
            if len(dice_name) <= 1:
                # Continuation
                cont_text = lines[current][1:]
            else:
                dice_name = dice_name[1]
                dice_name = re.sub(r'\.', '', dice_name)
            dice = re.findall(r'\(([\dd\+\-\s]*)\)', lines[current])
            dice_hit = re.findall(r'(\+\d+) to hit', lines[current])
            if len(dice_hit) > 0 and cont_text == '':
                melee = dice_name + ' ' + dice_hit[0] + ' (' + ' + '.join(dice) + ')'
            else:
                feats = mk_to_html(lines[current][1:].strip()) + '<br>'

        current += 1
    
    # Description
    descrip = ''
    current += 1
    while current < len(lines):
        if '|' in lines[current]:
            start = current
            while '|' in lines[current]:
                current += 1
            descrip += mk_table(lines[start:current])
        else:
            descrip += mk_to_html(lines[current])
        current += 1

    # Removing formatting error
    descrip = re.sub(r'\>\>', '>', descrip)

    # Derived Info
    BAB = str(max([eval(STR), eval(DEX)]))


    # Verify
    creatures[name] = {
        "AC": AC + ", touch " + AC + ", flat-footed " + AC,
        "AbilityScores": "Str " + STR + ", Dex " + DEX + ", Con " + CON + ", Int " + INT + ", Wis " + WIS + ", Cha " + CHA,
        "Alignment": align,
        "BaseAtk": BAB,
        "CMB": "N/A",
        "CMD": "N/A",
        "CR": CR,
        "Description": descrip,
        "Feats": feats,
        "HD": HD,
        "Immune": "{immune}",
        "Languages": lang,
        "Link": link,
        "Melee": melee,
        # bite +13 (2d6+5 plus grab), 2 stings +13 (1d6+5 plus poison), 2 wings +8 (1d6+2)
        "Ranged": "",
        "Resist": "{resist}",
        "Saves": "Fort +" + CON + ", Ref +" + DEX + ", Will +" + WIS,
        "Size": size,
        "Skills": skills,
        "Speed": speed,
        "Treasure": "standard",
        "Type": c_type,
        "Weaknesses": "{weak}",
        "XP": XP
    }

    print("___________________________________________________________________")

# pprint(creatures)
json.dump(creatures, open('5e_beasts.json', 'w', encoding='utf-8'), sort_keys=True, indent=4)

# creatures["{name}"] = {
#     "AC": "{AC}, touch {AC}, flat-footed {AC}",
#     "AbilityScores": "Str {STR}, Dex {DEX}, Con {CON}, Int {INT}, Wis {WIS}, Cha {CHA}",
#     "Alignment": "{align}",
#     "BaseAtk": "{BAB}",
#     "CMB": "N/A",
#     "CMD": "N/A",
#     "CR": "{CR}",
#     "Description": "{descrip}",
#     # "Feats": "",
#     "HD": "{HD}",
#     "Immune": "{immune}",
#     "Languages": "{lang}",
#     "Link": "{link}",
#     "Melee": "{melee}",
#     # bite +13 (2d6+5 plus grab), 2 stings +13 (1d6+5 plus poison), 2 wings +8 (1d6+2)
#     "Ranged": "{range}",
#     "Resist": "{resist}",
#     "Saves": "Fort +{CON}, Ref +{DEX}, Will +{WIS}",
#     "Size": "{size}",
#     "Skills": "{skills}",
#     "Speed": "{speed}",
#     "Treasure": "standard",
#     "Type": "{c_type}",
#     "Weaknesses": "{weak}",
#     "XP": "{XP}"
# }
