"""
Author: Hazmed Moreno & James Whittington
Program: Guitar Information Application
Class: Main
Version: 1.0.0
Release Date: 5.3.2022
Contact: hmoreno0@frostburg.edu
         jrwhittington0@frostburg.edu
Github: @hmorlive - Hazmed Moreno
        @vonravFSU - James Whittington
"""


import time
import utility


def run():
    """Runs the program"""
    try:
        print('\n--- |MAIN MENU| ---'
              '\nSelect from one of the following options: '
              '\n(1) Print guitar list'
              '\n(2) Search guitar in directory'
              '\n(3) Add guitar to directory'
              '\n(4) Delete guitar from directory'
              '\n(5) Exit')
        user_input = int(input('Selection: '))
        if user_input == 1:
            utility.print_guitar_list()
            run()
        elif user_input == 2:
            utility.check_list()
            run()
        elif user_input == 3:
            utility.append_to_file()
            run()
        elif user_input == 4:
            utility.delete_guitar()
            run()
        elif user_input == 5:
            print('---'
                  '\nThanks for using our program.')
            time.sleep(1)
            print('Goodbye', end=" ")
            time.sleep(.5)
            print('for now.')
            time.sleep(1)
            exit()
        else:
            print('Please enter a valid selection.'
                  '\nReturning to main.')
            time.sleep(2)
            run()

    except (Exception,):
        print('Oops... An error has occurred. Don\'t fear we will get to the bottom of this!'
              '\nRerunning program one more time.')
        time.sleep(2)
        utility.clear_all()
        run()


print('Welcome to Guitar Aid. This program is intended to help guitar selection.'
      '\nIf you are looking for a guitar (color, style, sound) you may find some help here.')
run()
