import eel
import simplejson as json


Names = []

# @eel.expose
def autofill_text(text):
    global Names
    p = len(text)
    s = 0
    e = len(Names) - 1
    # Binary Search based on starts with
    while e > s:
        m = (s + e) // 2
        print('Name  ', Names[m])
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
    print('Start ', s)
    print('Middle', m)
    print('End   ', e)
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


if __name__ == '__main__':
    Names = list(json.load(open("pokemon.json", 'r')).keys())
    Names.extend(list(json.load(open("beasts.json", 'r')).keys()))
    Names.sort()

    print(autofill_text('ak'))

    # # Set web files folder
    # eel.init('web')

    # # start
    # eel.start('monster.htm', size=(865, 750))
