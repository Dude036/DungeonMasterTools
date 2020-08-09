import eel


# Expose this function to Javascript
@eel.expose
def say_hello_py(x):
    print('Hello from ', x)


if __name__ == '__main__':
    # Set web files folder
    eel.init('web')

    # Call a Python Function
    say_hello_py('Python World!')

    # Call a Javascript function
    eel.say_hello_js('Python World!')

    # start
    eel.start('index.htm', size=(720, 480))
