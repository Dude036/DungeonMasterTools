import eel
import simplejson as json
from main import main
import os
import shutil


# Expose this function to Javascript
@eel.expose
def submit(settings, generate):
    print("Form has been submitted.")
    json.dump(generate, open('generate.json', 'w'), indent=4)
    json.dump(settings, open('settings.json', 'w'), indent=4)
    name = main()

    # Move the files up one folder
    p = os.listdir()
    # Get all files to move
    for file in p:
        if str(file).endswith('.town.json') or str(file).endswith('.html'):
            shutil.copyfile(file, os.path.join('web', file))
        elif str(file) == 'beasts' and os.path.isdir(file):
            try:
                os.mkdir(os.path.join('web', 'beasts'))
            except FileExistsError as e:
                print("Beasts folder already exists.")
            for bestiary in os.listdir(file):
                shutil.copyfile(os.path.join('beasts', bestiary), os.path.join(os.path.join('web', 'beasts'), bestiary))

    # Display to GUI
    eel.town_name_js(name)


if __name__ == '__main__':
    # Set web files folder
    eel.init('web')

    # start
    eel.start('index.htm', size=(865, 750))
