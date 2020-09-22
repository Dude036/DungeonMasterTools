import eel
import simplejson as json

def autofill_text():
    pass


if __name__ == '__main__':
    b_names = json.load(open("beasts.json", 'r'))
    p_names = json.load(open("pokemon.json", 'r'))    
    
    with open("names.txt", 'w') as outf:
        for name in list(b_names.keys()):
            outf.write(name + "\n")
        for name in list(p_names.keys()):
            outf.write(name + "\n")


    # # Set web files folder
    # eel.init('web')

    # # start
    # eel.start('monster.htm', size=(865, 750))
