==============================================================================================
==============================================================================================
Author: Hazmed Moreno & James Whittington
Program: Guitar Information Application
Version: 1.0.0
Release Date: 5.3.2022
Contact: hmoreno0@frostburg.edu
         jrwhittington0@frostburg.edu
Github: @hmorlive - Hazmed Moreno
        @vonravFSU - James Whittington
==============================================================================================
==============================================================================================
                                    ===================
                                    |Program Structure|
                                    ===================
Guitar Information App
    /data
        guitar_list.txt -> List of guitars w/ attributes
    /src
        main.py -> Runs the program
        utility.py -> Essential Program Functions
    guitar_tool.bat -> launches program on a Windows environment
    README.txt -> This file. Detailed program information
==============================================================================================
==============================================================================================
                                     =================
                                     |Class Structure|
                                     =================
----------------------------------------------------------------------------------------------
Class: Main
    run() -> Runs the program in a loop
----------------------------------------------------------------------------------------------
Class: Utility
    Variables:
        possible_guitars - list  -> listfor printing possible guitars
        guitar_counter - list  -> list for popularity counter
        guitar_cost - list  -> list for costs of guitars
        master_list - list of sets -> list of sets for reading guitars
        temp_set - set  -> temporary set for reading into master_list
        guitar_set - set  -> temporary set to write into master_list
        file_location - str -> txt file location

    Methods:
        def load_items() -> Loads each guitar and its corresponding attributes into a set
                            & Loads each set into master list
        def append_to_file() -> Appends guitar to file
        def write_to_file() -> Writes guitars to file
        def print_guitar_list() -> Prints the name of all available guitars
        def check_list() -> Checks if user entry is subset of sets in master list
        def print_ordered_list(name, count, cost): -> Orders guitar list by cost ASC (TimSort)
                                                      params: name (list), count (list), cost (list)
        def delete_guitar() -> Deletes guitar from master list and rewrites to file
        def check_if_empty() -> Checks if guitar list is empty
        def wait_for_user() -> Waits for user to press ENTER to continue
----------------------------------------------------------------------------------------------
==============================================================================================