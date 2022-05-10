"""
Author: Hazmed Moreno & James Whittington
Program: Guitar Information Application
Class: Utility
Version: 1.0.0
Release Date: 5.3.2022
Contact: hmoreno0@frostburg.edu
         jrwhittington0@frostburg.edu
Github: @hmorlive - Hazmed Moreno
        @vonravFSU - James Whittington
"""

import re


# Declaring Variables
possible_guitars = list()  # array list for printing possible guitars
guitar_counter = list()  # array list for popularity counter
guitar_cost = list()  # array list for costs of guitars
master_list = list(set())  # list of sets for reading guitars
temp_set = set()  # temporary set for reading into master_list
guitar_set = set()  # temporary set to write into master_list
file_location = 'data/guitar_list.txt'  # guitar list location


def load_items():
    """Loads each guitar and its corresponding attributes into a set
       and each set into master list"""
    with open(file_location, 'r') as f:
        for line in f:
            if any(c == '%' for c in line):
                if len(temp_set) != 0:
                    master_list.append(set(temp_set))
                    temp_set.clear()
            else:
                temp_set.add(line.strip())
    master_list.append(set(temp_set))
    temp_set.clear()


def append_to_file():
    """Appends guitar to file"""
    attribute = ' '
    guitar_name = input('Enter guitar name: ')
    g_cost = input('Enter guitar cost or (0) if not available: ')

    while attribute != '':
        attribute = (input('Enter attribute or Press |ENTER| when done: ')).lower()
        if attribute == '':
            break
        temp_set.add(attribute)
    with open(file_location, 'a') as f:
        f.write('%\n' + 'name: ' + guitar_name
                + '\n' + 'counter: ' + '0' +
                '\n' + 'cost: ' + str(g_cost) + '\n')
        for i in temp_set:
            f.write(i + '\n')
    f.close()
    temp_set.clear()
    master_list.clear()


def write_to_file():
    """Writes guitars to file"""

    with open(file_location, 'w') as f:
        for item in master_list:
            f.write('%\n')
            for i in item:
                f.write(i + '\n')
    f.close()
    master_list.clear()


def print_guitar_list():
    """Prints the name of all available guitars"""

    load_items()
    if check_if_empty():
        return

    # Iterates through every set in master list and grabs name, counter, and cost
    for count in range(len(master_list)):
        for i in master_list[count]:
            if re.match("name", i):
                i = i.removeprefix("name: ")
                possible_guitars.append(i)
            elif re.match("counter", i):
                i = i.removeprefix("counter: ")
                guitar_counter.append(i)
            elif re.match("cost", i):
                i = i.removeprefix("cost: ")
                guitar_cost.append(i)
    print_ordered_list(possible_guitars, guitar_counter, guitar_cost)


def check_list():
    """Makes user entry a subset and checks if it is a subset
        of the sets in master list"""

    load_items()
    if check_if_empty():
        return
    attribute = ' '

    while attribute != '':
        attribute = (input('Enter attribute or Press |ENTER| when done: ')).lower()
        if attribute == '':
            break
        temp_set.add(attribute)
    print('---')
    for count in range(len(master_list)):
        if temp_set.issubset(master_list[count]):
            for i in master_list[count]:
                if re.match("name:", i):
                    guitar_set.add(i)
                    i = i.removeprefix("name: ")
                    possible_guitars.append(i)
                elif re.match("counter:", i):
                    i = i.removeprefix("counter: ")
                    guitar_counter.append(i)
                    g_count = int(i)
                    i = 'counter: ' + str(g_count + 1)
                    guitar_set.add(i)
                elif re.match("cost:", i):
                    guitar_set.add(i)
                    i = i.removeprefix("cost: ")
                    guitar_cost.append(i)
                else:
                    guitar_set.add(i)
            master_list[count] = set(guitar_set)
            guitar_set.clear()

    temp_set.clear()
    print_ordered_list(possible_guitars, guitar_counter, guitar_cost)


def print_ordered_list(name, count, cost):
    """Prints ordered guitar list by cost ASC
    :param list name: Guitar Names
    :param list count: Guitar Popularity Count
    :param list cost: Guitar Cost"""

    sorting_list = list(list())  # temporary list of lists to sort guitars by price
    temp_list = list()  # temporary list
    num = 0

    print('Guitars matching term(s) sorted by price ASC: ')
    if len(name) != 0:
        g_count = 0
        for i in name:
            temp_list.append(i)
            temp_list.append(count[g_count])
            temp_list.append(float(cost[g_count]))
            sorting_list.append(list(temp_list))
            temp_list.clear()
            g_count += 1

        # Sorting List By Price Using TimSort
        sorting_list.sort(key=lambda x: x[2])  # big O = n (log(n)

        for i in sorting_list:
            num += 1
            print(num, i[0],
                  '| Popularity: ', i[1],
                  ' | Cost: $', i[2])

    else:
        print('No guitars found based on entered attribute')
    print('---')

    # clearing set and lists.
    guitar_counter.clear()
    guitar_cost.clear()
    possible_guitars.clear()
    guitar_set.clear()
    sorting_list.clear()
    write_to_file()
    wait_for_user()


def delete_guitar():
    """Deletes guitar from master list and rewrites master list to file"""

    load_items()
    g_count = 0

    if check_if_empty():
        return

    for count in range(len(master_list)):
        for i in master_list[count]:
            if re.match("name:", i):
                i = i.removeprefix("name: ")
                possible_guitars.append(i)

    for i in possible_guitars:
        g_count += 1
        print(g_count, i)

    num = int(input('Select guitar to delete: ')) - 1
    master_list.pop(num)
    print('Guitar removed')
    write_to_file()
    possible_guitars.clear()
    wait_for_user()


def check_if_empty():
    """Checks if guitar list is empty
    :returns: true if master list is empty"""

    if not master_list[0]:
        print('Sorry, the guitar list is empty. Try adding some.')
        wait_for_user()
        return True
    return False


def wait_for_user():
    """Waits for user to press ENTER to continue"""

    status = ' '
    while status != '':
        status = input('Press |ENTER| to continue')
        if status == '':
            break


def clear_all():
    """Clears all sets and lists"""
    possible_guitars.clear()
    guitar_counter.clear()
    guitar_cost.clear()
    master_list.clear()
    temp_set.clear()
    guitar_set.clear()
