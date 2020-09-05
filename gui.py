import eel
from names import TownNamer
from pprint import pprint
import simplejson as json
from main import main


# Expose this function to Javascript
@eel.expose
def submit(settings, generate):
    print("Form has been submitted.")
    json.dump(generate, open('generate.json', 'w'), indent=4)
    json.dump(settings, open('settings.json', 'w'), indent=4)
    name = main()
    eel.town_name_js(name)


if __name__ == '__main__':
    # Set web files folder
    eel.init('web')

    # start
    eel.start('index.htm', size=(850, 750))
