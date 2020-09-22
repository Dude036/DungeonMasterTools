import eel
import simplejson as json


Names = []

# @eel.expose
def autofill_text(text: str):
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
    if s == e:
        print("No suggestion")
        return []
    
    print('Start ', s)
    print('Middle', m)
    print('End   ', e)
    return []


if __name__ == '__main__':
    Names = list(json.load(open("pokemon.json", 'r')).keys())
    Names.extend(list(json.load(open("beasts.json", 'r')).keys()))
    Names.sort()

    autofill_text('abra')

    # # Set web files folder
    # eel.init('web')

    # # start
    # eel.start('monster.htm', size=(865, 750))
