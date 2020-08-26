import eel
from names import TownNamer
from pprint import pprint
import simplejson as json
from main import main


# Expose this function to Javascript
@eel.expose
def say_hello_py(x):
    print('Hello from ', x)


@eel.expose
def submit(settings, generate):
    print("Form has been submitted.")
    print("Settings:")
    pprint(settings)
    print("Generate:")
    pprint(generate)
    json.dump(generate, open('generate.json', 'w'), indent=4)
    json.dump(settings, open('settings.json', 'w'), indent=4)
    main()

if __name__ == '__main__':
    # Set web files folder
    eel.init('web')

    # Call a Python Function
    say_hello_py('Python World!')

    # Call a Javascript function
    eel.say_hello_js('Python World!')

    # start
    eel.start('index.htm', size=(850, 750))
