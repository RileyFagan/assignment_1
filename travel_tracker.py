"""
Name: Riley Fagan
Date started: 04/09/2020
GitHub URL: https://github.com/RileyFagan/assignment_1
"""

import csv

MENU = """Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit"""

file_list = []
with open("places.csv", "r") as places_file:
    places_data = csv.reader(places_file)
    for line in places_data:
        file_list.append(line)
print("Travel Tracker 1.0 - by Riley Fagan")
print(len(file_list), "places loaded from", places_file.name)


def main(file_list):
    places_list = file_list
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_locations(places_list)
        elif choice == "A":
            location = add_location()
            places_list.append(location)
        elif choice == "M":
            places_list = visited_location(places_list)
        else:
            print("invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Have a nice day! :)")
    with open("places.csv", "w", newline="") as file:
        places_data = csv.writer(file)
        places_data.writerows(places_list)
    print(len(places_list), " have been saved to", file.name)


# combine location details and priority to list
def add_location():
    location_list = [location_name(), location_country(), location_priority(), "n"]
    print(location_list[0], "in", location_list[1], "(priority", location_list[2], ") added to Travel Tracker")
    return location_list


# get name of location
def location_name():
    name = input("Name:")
    while len(name) == 0:
        print("Input can not be blank")
        name = input("Name:")
    return name


# get name of country
def location_country():
    country = input("Country:")
    while len(country) == 0:
        print("Input can not be blank")
        country = input("Country:")
    return country


# get priority number
def location_priority():
    input_text = "Priority:"
    priority = int_error_check(input_text)
    while priority < 0:
        print("Number must be > 0")
        priority = int_error_check(input_text)
    return priority


# int error checking
def int_error_check(input_text):
    while True:
        try:
            value = int(input(input_text))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            return value


# lists locations
def list_locations(places_list):
    for i, places in enumerate(places_list):
        if places[3] == 'n':
            print("*", i + 1, ".", places[0], "in", places[1], "priority", places[2])
        else:
            print(" ", i + 1, ".", places[0], "in", places[1], "priority", places[2])
    print(len(places_list), "places. You still want to visit", places_not_visited(places_list), "places")


# calculate places not visited
def places_not_visited(places_list):
    places_not_visited = 0
    for places in places_list:
        if places[3] == 'n':
            places_not_visited += 1
        else:
            places_not_visited += 0
    return places_not_visited

# edit place_list to mark place as visited
def visited_location(places_list):
    list_locations(places_list)
    visited_input = visited_location_error_check(places_list)
    if places_list[visited_input][3] == 'v':
        print("That place is already visited")
    if places_list[visited_input][3] == 'n':
        print(places_list[visited_input][0], "in", places_list[visited_input][1], "Visited!")
        places_list[visited_input][3] = 'v'
    return places_list


# Visited location error checking
def visited_location_error_check(places_list):
    print("Enter the number of a place to mark as visited")
    input_text = ">>> "
    visited_input = int_error_check(input_text)
    visited_input -= 1
    index_length = (len(places_list))
    index_length -= 1
    while visited_input < 0 or visited_input > index_length:
        print("Invalid input, enter valid number")
        visited_input = int_error_check(input_text)
    return visited_input


main(file_list)
