import eel
import simplejson as json
from beastiary import pick_monster, print_monster, Beasts, Poke_moves
from numpy.random import choice

Names = []
Stats = {}


@eel.expose
def autofill_text(text):
    global Names
    p = len(text)
    s = 0
    e = len(Names) - 1
    # Binary Search based on starts with
    while e > s:
        m = (s + e) // 2
        print('Found ', Names[m])
        if Names[m][:p].lower() < text.lower():
            s = m + 1
        elif Names[m][:p].lower() > text.lower():
            e = m + 1
        else:
            print("Breaking")
            break

    # Validate if there's a reason to continue looking
    if s >= e:
        print("No suggestion")
        return []

    # Loop to find all potential
    found = set()
    it = 0
    for name in reversed(Names[s:m]):
        it += 1
        if name.lower().startswith(text):
            found.add(name)
        else:
            break
    for name in Names[m:e]:
        it += 1
        if name.lower().startswith(text):
            found.add(name)
        else:
            break

    print(it)
    return list(found)


@eel.expose
def submit(name, cr):
    global Names, Stats
    print(type(name), ':', name)
    print(type(cr), ':', cr)

    if name == '' or name not in Names:
        print("Unable to find monster, Generating random")
        name = choice(list(Stats.keys()))
        monster = Stats[name]
        while monster['CR'] != cr:
            name = choice(list(Stats.keys()))
            monster = Stats[name]
    else:
        monster = Stats[name]

    # Print off final
    mon_html = print_monster([name, monster], False)
    return mon_html


if __name__ == '__main__':
    # Sort the names of all the creatures
    Names = list(json.load(open("pokemon.json", 'r')).keys())
    Names.extend(list(json.load(open("beasts.json", 'r')).keys()))
    Names.extend(list(json.load(open("5e_beasts.json", 'r')).keys()))
    Names.sort()

    # Get all monster Stats
    Stats.update(json.load(open('beasts.json', 'r'), encoding='utf-8'))
    Stats.update(json.load(open('5e_beasts.json', 'r'), encoding='utf-8'))
    Stats.update(json.load(open('pokemon.json', 'r'), encoding='utf-8'))
    Poke_moves.update(json.load(open('pokemon_moves.json', 'r'), encoding='utf-8'))

    # Set web files folder
    eel.init('web')

    # start
    eel.start('monster.htm', size=(865, 750))
