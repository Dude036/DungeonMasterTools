#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
from stores import *
import quests
import PC
from character import create_person
from variance import create_variance
import simplejson as json

townHTML = '<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width" /><title></title><style>' \
           'body{max-width:800px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px;} html{' \
           'font-family:Arial;}h1, h2 {color:black;text-align:center;} .center{text-align:center;} .bold{font-weight:' \
           'bold;}.emp{font-style:italic;} table{border:1px solid black;border-spacing:0px;}table tr th {' \
           'background-color:gray;color:white;padding:5px;}table tr td {margin:0px;padding:5px;}.text-xs{font-size:' \
           '12px;}.text-sm{font-size:14px;}.text-md{font-size:18px;}.text-lg{font-size:24px;}.text-xl{font-size:' \
           '32px;}.col-1-3{width:33.3%;float: left;}.col-2-3{width:50%;float:left;}.col-3-3{width:100%;float:left;}' \
           '.col-1-2{width:50%;float:left;}.col-2-2{width:100%;float:left;}.col-1-4{width:25%;float:left;}.col-2-4{' \
           'width:33.3%;float:left;}.col-3-4{width:50%;float:left;}.col-4-4{width:100%;float:left;}</style><style ' \
           'type="text/css">.inventory-table td{border-bottom:1px solid black;}.wrapper-box{width:100%;border:2px ' \
           'solid black;padding:5px;}</style></head><body><script>function show_hide(ident){\nvar a = document.' \
           'getElementById(ident);\nif (a.style.display === \'none\'){\na.style.display = \'block\';} else {' \
           'a.style.display = \'none\';}}</script>'

store_head = """<table class="wrapper-box" style="margin-bottom:60px;"><tr><td><span class="text-lg bold">"""
notable_head = '<table class="wrapper-box"><tr><td><span class="bold text-md">'
inventory_head_rarity = '</div><span class="text-lg bold">Inventory <span class="text-sm emp"> - Inflation:</span>' \
                        '</span><table style="width:100%;" class="inventory-table"><tr><th style="text-align:left;">' \
                        'Item</th><th style="text-align:left;">Cost</th><th style="text-align:left;">Rarity</th></tr>'
inventory_head_type = '</div><span class="text-lg bold">Inventory <span class="text-sm emp"> - Inflation:</span>' \
                      '</span><table style="width:100%;" class="inventory-table"><tr><th style="text-align:left;">' \
                      'Item</th><th style="text-align:left;">Cost</th><th style="text-align:left;">Type</th></tr>'
characters = []
Notable = False


def write_store(store, rarity=True):
    global townHTML
    info = store_head + store.Store_name + """</span><br />\n<span class="bold text-md">Proprietor: </span><span""" + \
           """ class="text-md">"""
    info += str(store.Shopkeeper)
    if rarity:
        info += inventory_head_rarity
        info = info.replace(
            "Inflation:",
            "Inflation: " + str(round(store.Inflation * 100, 2)) + "%")
    else:
        info += inventory_head_type
        info = info.replace(
            "Inflation:",
            "Inflation: " + str(round(store.Inflation * 100, 2)) + "%")

    for x in range(len(store.Stock)):
        info += str(store.Stock[x])

    info += """</table></td></tr></table><br />"""

    townHTML += info


def write_html(name=''):
    global townHTML
    if name == '':
        name = 'test'
    with open(name + '.html', 'w') as outf:
        outf.write(bs(townHTML, 'html5lib').prettify())


def write_npc(character, position):
    global townHTML, Notable
    if not Notable:
        townHTML += '<div style="page-break-after:always;"></div><h2 class="text-lg bold center">Notable People</h2>'
        Notable = True
    townHTML += notable_head + position + ': </span><span class="text-md">' + str(
        character)
    townHTML += '</div></td></tr></table><br />'


def write_people(person, position):
    global townHTML, Notable
    if not Notable:
        townHTML += '<div style="page-break-after:always;"></div><h2 class="text-lg bold center">Notable People</h2>'
        Notable = True
    townHTML += notable_head + position + ': </span><span class="text-md">' + str(
        person)
    townHTML += '</div></td></tr></table><br />'


def generate_shops(w, a, p, e, en, b, t, j, f, g, br, gu, v, qu, name='', dump_json=False):
    """ [# of Stores, Rarity Low, Rarity High, Quan High, Quan Low] """
    global townHTML
    from names import TownNamer
    town_name = str(TownNamer()) if name == '' else name
    townHTML += "<h1>" + town_name + "</h1><p>Description</p>"
    if sum([w[0], a[0], p[0], e[0], en[0], b[0], t[0], j[0], f[0], g[0], br[0], gu[0]]) > 0:
        townHTML += """<h2 class="text-lg bold center">Shops</h2>"""
    full_town = {}
    i = 0
    for _ in range(w[0]):
        store = create_weapon_shop(
            create_person(create_variance()), [w[1], w[2]],
            randint(w[3], w[4]),
            inflate=w[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(a[0]):
        store = create_armor_shop(
            create_person(create_variance()), [a[1], a[2]],
            randint(a[3], a[4]),
            inflate=a[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(p[0]):
        store = create_potion_shop(
            create_person(create_variance()), [p[1], p[2]],
            randint(p[3], p[4]),
            inflate=p[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(e[0]):
        store = create_enchantment_shop(
            create_person(create_variance()), [e[1], e[2]],
            randint(e[3], e[4]),
            inflate=e[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(en[0]):
        store = create_enchanter_shop(
            create_person(create_variance()), [en[1], en[2]],
            randint(en[3], en[4]),
            inflate=en[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(b[0]):
        store = create_book_shop(
            create_person(create_variance()),
            choice(Books.Genres, randint(len(Books.Genres)), replace=False),
            randint(b[1], b[2]),
            inflate=b[3])
        write_store(store, False)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(t[0]):
        store = create_tavern(
            create_person(create_variance()),
            t[1],
            randint(t[2], t[3]),
            inflate=t[4])
        write_store(store, False)
        full_town[i] = store.__dict__
        i += 1

    for _ in range(j[0]):
        store = create_jewel_shop(
            create_person(create_variance()), [j[1], j[2]],
            randint(j[3], j[4]),
            inflate=j[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(f[0]):
        store = create_restaurant(
            create_person(create_variance()),
            randint(f[1], f[2]),
            inflate=f[3])
        write_store(store)
        full_town[i] = store.__dict__
        i += 1

    for _ in range(g[0]):
        store = create_general_store(
            create_person(create_variance()), [g[1], g[2]],
            randint(g[3], g[4]),
            g[5],
            inflate=g[6])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(br[0]):
        store = create_brothel(
            create_person(create_variance()),
            randint(br[1], br[2]),
            inflate=br[3])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(gu[0]):
        store = create_gunsmith(
            create_person(create_variance()), [gu[1], gu[2]],
            randint(gu[3], gu[4]),
            inflate=gu[5])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(v[0]):
        store = create_variety_shop(
            create_person(create_variance()),
            randint(v[1], v[2]),
            inflate=v[3])
        write_store(store)
        full_town[i] = store.to_dict()
        i += 1

    for _ in range(qu[0]):
        q = quests.QuestBoard(qu[1], qu[2], qu[3], town_name)
        townHTML += str(q)
        full_town[i] = q.__dict__
        i += 1

    # Dump the class information into a json file
    if dump_json:
        json.dump(full_town, open(town_name + ".town.json", 'w'), indent=4, sort_keys=True, default=lambda x: x.__dict__)
    return town_name


def generate_people(pc, npc, town_name, dump_json=False):
    full_town = {}
    if dump_json:
        full_town = json.load(open(town_name + '.town.json', 'r'))

    for p in pc:
        person = create_person(create_variance())
        write_people(person, p)
        full_town[p] = person

    for p in npc:
        person = PC.PC()
        write_npc(person, p)
        full_town[p] = person

    if dump_json:
        json.dump(full_town, open(town_name + ".town.json", 'w'), indent=4, sort_keys=True, default=lambda x: x.__dict__)

    print("Writing the town ", town_name)
    write_html(town_name)



if __name__ == '__main__':
    townHTML += """<h2 class="text-lg bold center">Shops</h2>"""
    for _ in range(4):
        write_store(
            create_weapon_shop(
                create_person(create_variance()), [0, 2],
                randint(5, 15),
                inflate=4))

        write_store(
            create_armor_shop(
                create_person(create_variance()), [0, 2],
                randint(5, 15),
                inflate=4))

        write_store(
            create_potion_shop(
                create_person(create_variance()), [0, 9],
                randint(5, 15),
                inflate=4))

        write_store(
            create_enchantment_shop(
                create_person(create_variance()), [0, 9],
                randint(15, 25),
                inflate=4))

        write_store(
            create_enchanter_shop(
                create_person(create_variance()), [0, 9],
                randint(15, 25),
                inflate=4))

        write_store(
            create_book_shop(
                create_person(create_variance()),
                choice(
                    Books.Genres, randint(len(Books.Genres)), replace=False),
                randint(15, 25),
                inflate=4), False)

        write_store(
            create_tavern(create_person(create_variance()), 0, 3, 15), False)

        write_store(
            create_jewel_shop(
                create_person(create_variance()), [0, 5],
                randint(15, 30),
                inflate=4))

        write_store(
            create_restaurant(
                create_person(create_variance()), randint(15, 30), inflate=4),
            False)

        write_store(
            create_general_store(
                create_person(create_variance()), [0, 1],
                randint(10, 20),
                randint(1, 5),
                inflate=4), False)

    townHTML += '<div style="page-break-after:always;"></div><h2 class="text-lg bold center">Notable People</h2>'
    for _ in range(1):
        # Notable people
        write_people(create_person(create_variance()), 'Mayor')
        write_people(create_person(create_variance()), 'Captain of the Guard')
        write_people(create_person(create_variance()), 'Holy Person')
        write_npc(create_person(create_variance()), 'Gladiator')
        write_npc(create_person(create_variance()), 'Thief')
        write_npc(create_person(create_variance()), 'Guard')

    write_html()
