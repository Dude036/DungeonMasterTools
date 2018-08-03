#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
from numpy.random import choice, randint
import name_generator as ng
from traits import *
from stores import *
from variance import create_variance

townHTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width" /><title></title>""" + \
      """<style>body {max-width:800px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px;} html{font-family:Arial;}""" + \
      """h1, h2 {color:black;text-align:center;} .center{text-align:center;} .bold{font-weight:bold;}""" + \
      """.emp{font-style:italic;} table{border:1px solid black;border-spacing:0px;}""" + \
      """table tr th {background-color:gray;color:white;padding:5px;}table tr td {margin:0px;padding:5px;}""" + \
      """.text-xs{font-size:12px;}.text-sm{font-size:14px;}.text-md{font-size:18px;}""" + \
      """.text-lg{font-size:24px;}.text-xl{font-size:32px;}.col-1-3{width:33.3%;float: left;}""" + \
      """.col-2-3{width:50%;float:left;}.col-3-3{width:100%;float:left;}.col-1-2{width:50%;float:left;}""" + \
      """.col-2-2{width:100%;float:left;}.col-1-4{width:25%;float:left;}.col-2-4{width:33.3%;float:left;}""" + \
      """.col-3-4{width:50%;float:left;}.col-4-4{width:100%;float:left;}</style>""" + \
      """<style type="text/css">.inventory-table td{border-bottom:1px solid black;}.wrapper-box{width:100%;border:2px solid black;padding:5px;}</style></head><body>""" + \
      """<script>function show_hide(ident){\nvar a = document.getElementById(ident);\nif (a.style.display === 'none'){\n""" + \
      """a.style.display = 'block';} else {a.style.display = 'none';}}</script>"""

store_head = """<table class="wrapper-box" style="margin-bottom:60px;"><tr><td><span class="text-lg bold">"""
notable_head = '<table class="wrapper-box"><tr><td><span class="bold text-md">'
inventory_head_rarity = """</div><span class="text-lg bold">Inventory <span class="text-sm emp"> - Inflation:</span></span><table style="width:100%;" class="inventory-table"><tr><th style="text-align:left;">Item</th><th style="text-align:left;">Cost</th><th style="text-align:left;">Rarity</th></tr>"""
inventory_head_type = """</div><span class="text-lg bold">Inventory <span class="text-sm emp"> - Inflation:</span></span><table style="width:100%;" class="inventory-table"><tr><th style="text-align:left;">Item</th><th style="text-align:left;">Cost</th><th style="text-align:left;">Type</th></tr>"""
characters = []
Notable = False

class Character(object):
    """Characters are the centerpiece of stories"""
    Name = Gender = Race = Appearance = ''
    Traits = Story = []
    Age = 0

    def __init__(self, cName, cRace, cGender, cAge, cAppearance, cTraits, cStory):
        self.Name = cName
        self.Race = cRace
        self.Gender = cGender
        self.Age = cAge
        self.Appearance = cAppearance
        self.Traits = cTraits
        self.Story = cStory

    def __str__(self):
        info = self.Name + """<div>""" + \
               """<ul><li><span style="font-weight:bold;">Race:</span> """ + self.Race + \
               """</li><li><span style="font-weight:bold;">Gender:</span> """ + self.Gender + \
               """</li><li><span style="font-weight:bold;">Age:</span> """ + str(self.Age) + \
               """</li><li><span style="font-weight:bold;">Appearance:</span> """ + str(self.Appearance) + \
               """</li><li><span style="font-weight:bold;">Trait 1:</span> """ + self.Traits[0] + "</li>"
        if len(self.Traits) > 1:
            info += """<li><span style="font-weight:bold;">Trait 2:</span> """ + self.Traits[1] + "</li>"
        info += "</ul><p>"
        for x in range(len(self.Story)):
            info += self.Story[x] + """</p>"""
            if x + 1 < len(self.Story):
                info += """<p>"""
        return info


def load_character(filename):
    paragraph = []
    n = r = g = ap = ''
    ag = 0
    with open(filename, 'r') as f:
        content = f.readlines()
    n = content[0].strip()
    r = content[1].strip()
    g = content[2].strip()
    ag = int(content[3].strip())
    tr = content[4].strip()
    ap = [content[5].strip(), content[6].strip(), ]
    for line in range(7, len(content)):
        paragraph.append(content[line].strip())
    return Character(n, r, g, ag, ap, tr, paragraph)


def create_person(pop):
    race = choice(list(pop.keys()), 1, p=list(pop.values()))
    gender = choice(['Male', 'Female'])
    name = ng.name_parser(race, gender)
    age = randint(ages[race[0]][0], ages[race[0]][1])

    face = appearance['Face'][randint(len(appearance['Face']))]
    hair = appearance['Hair'][randint(len(appearance['Hair']))]
    eyes = appearance['Eyes'][randint(len(appearance['Eyes']))]
    body = appearance['Body'][randint(len(appearance['Body']))]
    appear = body + ' and looks ' + face.lower() + ' with ' + hair.lower() + ' hair and ' + eyes.lower() + ' eyes. '

    back = 'I\'m a ' + gender + ' ' + race[0] + ', from '
    back += back_location[randint(len(back_location))] + ' who '
    back += back_story[randint(len(back_story))]

    trait = []
    demenor = randint(3)
    if demenor == 2:
        trait.append(positive_traits[randint(len(positive_traits))])
        trait.append(positive_traits[randint(len(positive_traits))])
    elif demenor == 1:
        trait.append(neutral_traits[randint(len(neutral_traits))])
        trait.append(neutral_traits[randint(len(neutral_traits))])
    else:
        trait.append(negative_traits[randint(len(negative_traits))])
        trait.append(negative_traits[randint(len(negative_traits))])

    story = [back, ]

    return Character(name, race[0], gender, age, appear, trait, story)


def write_store(store, rarity=True):
    global townHTML
    info = store_head + store.Store_name + """</span><br />\n<span class="bold text-md">Proprietor: </span><span class="text-md">"""
    info += str(store.Shopkeeper)
    if rarity:
        info += inventory_head_rarity
        info = info.replace("Inflation:", "Inflation: " + str(round(store.Inflation*100, 2)) + "%")
    else:
        info += inventory_head_type
        info = info.replace("Inflation:", "Inflation: " + str(round(store.Inflation*100, 2)) + "%")

    for x in range(len(store.Stock)):
        info += str(store.Stock[x])

    info += """</table></td></tr></table><br />"""

    townHTML += info


def write_html():
    global townHTML
    with open('test.html', 'w') as outf:
        outf.write(bs(townHTML, 'html5lib').prettify())


def write_people(person, position):
    global townHTML, Notable
    if not Notable:
        townHTML += '<div style="page-break-after:always;"></div><h2 class="text-lg bold center">Notable People</h2>'
        Notable = True
    townHTML += notable_head + position + ': </span><span class="text-md">' + str(person)
    townHTML += '</div></td></tr></table><br />'


def generate(w, a, p, e, en, b, t, j, f, g):
    """ [# of Stores, Rarity Low, Rarity High, Quan High, Quan Low] """
    global townHTML
    if sum([w[0], a[0], p[0], e[0], en[0], b[0], t[0], j[0], f[0], g[0]]) > 0:
        townHTML += """<h2 class="text-lg bold center">Shops</h2>"""

    for _ in range(w[0]):
        store = create_weapon_shop(create_person(create_variance()), [w[1], w[2]], randint(w[3], w[4]), inflate=w[0])
        write_store(store)

    for _ in range(a[0]):
        store = create_armor_shop(create_person(create_variance()), [a[1], a[2]], randint(a[3], a[4]), inflate=a[0])
        write_store(store)
        
    for _ in range(p[0]):
        store = create_potion_shop(create_person(create_variance()), [p[1], p[2]], randint(p[3], p[4]), inflate=p[0])
        write_store(store)
        
    for _ in range(e[0]):
        store = create_enchantment_shop(create_person(create_variance()), [e[1], e[2]], randint(e[3], e[4]), inflate=e[0])
        write_store(store)
        
    for _ in range(en[0]):
        store = create_enchanter_shop(create_person(create_variance()), [en[1], en[2]], randint(en[3], en[4]), inflate=en[0])
        write_store(store)
        
    for _ in range(b[0]):
        store = create_book_shop(create_person(create_variance()),
                                 choice(Books.Genres, randint(len(Books.Genres)), replace=False),
                                 randint(b[1], b[2]), inflate=b[0])
        write_store(store, False)
        
    for _ in range(t[0]):
        # [Quality, Rooms, Quantity Low, Quantity High]
        store = create_tavern(create_person(create_variance()), t[1], t[2], randint(t[3], t[4]), inflate=t[0])
        write_store(store, False)
        
    for _ in range(j[0]):
        store = create_jewel_shop(create_person(create_variance()), [j[1], j[2]], randint(j[3], j[4]), inflate=j[0])
        write_store(store)
        
    for _ in range(f[0]):
        store = create_restaurant(create_person(create_variance()), f[1], randint(f[2], f[3]), inflate=f[0])
        write_store(store)
        
    for _ in range(g[0]):
        store = create_general_store(create_person(create_variance()), [g[1], g[2]], randint(g[3], g[4]), g[5], inflate=g[0])
        write_store(store)



if __name__ == '__main__':
    townHTML += """<h2 class="text-lg bold center">Shops</h2>"""
    for _ in range(4):
        w = create_weapon_shop(create_person(create_variance()), [0, 2], randint(5, 15), inflate=4)
        write_store(w)

        w = create_armor_shop(create_person(create_variance()), [0, 2], randint(5, 15), inflate=4)
        write_store(w)

        w = create_potion_shop(create_person(create_variance()), [0, 9], randint(5, 15), inflate=4)
        write_store(w)

        w = create_enchantment_shop(create_person(create_variance()), [0, 9], randint(15, 25), inflate=4)
        write_store(w)

        w = create_enchanter_shop(create_person(create_variance()), [0, 9], randint(15, 25), inflate=4)
        write_store(w)

        write_store(create_book_shop(create_person(create_variance()),
                                     choice(Books.Genres, randint(len(Books.Genres)), replace=False),
                                     randint(15, 25), inflate=4), False)

        w = create_tavern(create_person(create_variance()), 0, 3, 15)
        write_store(w, False)

        w = create_jewel_shop(create_person(create_variance()), [0, 5], randint(15, 30), inflate=4)
        write_store(w)

        w = create_restaurant(create_person(create_variance()), 0, randint(15, 30), inflate=4)
        write_store(w, False)

        w = create_general_store(create_person(create_variance()), [0, 1], randint(10, 20), inflate=4)
        write_store(w, False)

    townHTML += '<div style="page-break-after:always;"></div><h2 class="text-lg bold center">Notable People</h2>'
    for _ in range(1):
        # Notable people
        write_people(create_person(create_variance()), 'Mayor')
        write_people(create_person(create_variance()), 'Captain of the Guard')
        write_people(create_person(create_variance()), 'Holy Person')


    write_html()
    load_character('character.txt')
    create_person(create_variance())



