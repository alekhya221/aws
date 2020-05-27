"""The module echo

This is the "echo" module, providing some useless functions!
"""


def func1():
    print("echo function func1 has been called!")


def func2():
    print("echo function func2 has been called!")


def func3():
    from .reverse import reverse_sound
    #from sound.filters.equalizer import print_equalizer
    from ..filters.equalizer import print_equalizer
    print("echo function func3 has been called!")
    reverse_sound()
    print_equalizer()

def print_echo():
    print('Echo Echo!')
    
    


print("Module echo.py has been loaded!")
func3()

