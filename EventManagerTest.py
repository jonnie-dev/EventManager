"""
Author: Md. Aminul(Jonnie) Islam
ID: 12312185
Email: 12312185@cqumail.com
Contact: 0433927014
Unit Name: Introduction to Programming
Tutor: Shouthiri Partheepan
CQ University, Sydney Campus
400 Kent Street, Sydney
NSW 2000, Australia
=============================================================
 ASSIGNMENT: Sydney Yummy Catering Event Management System 
=============================================================
The system is to:
  1. Define an Event class with 4 attributes: name, date, location, guests
  2. Validate the date format (yyyy-mm-dd)
  3. Validate guest count (must be between 5 and 500 inclusive)
  4. Store all events in a list managed by an EventManager class
  5. Save the event list to a text file
  6. Load existing events from that text file on startup
  7. Search for events by name (case-insensitive, partial match)
"""

import datetime
from Event import Event
from EventManager import EventManager

# TODO 2 - validate_date() function


def validate_date(date_str):
    """Accepts a string and returns True if it matches yyyy-mm-dd AND
       represents a real calendar date; otherwise returns False."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# TODO 3 - validate non empty input


def get_non_empty(prompt):
    """Prompt until a non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

# TODO 4 - validate guest number input


def get_positive_int(prompt):
    """Prompt until the user enters a whole number between 5 and 500 (inclusive)."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Please enter a numeric value.")
            continue
        if not value.isdigit():
            print("Please enter a whole number.")
            continue
        guests = int(value)
        if 5 <= guests <= 500:
            return guests
        print("Please enter a number between 5 and 500.")

# TODO 5 - show_menu function


def show_menu():
    """Display the menu and return the user's choice as a string."""
    print()
    print("Menu:")
    print("1. Add event")
    print("2. Display events")
    print("3. Save events")
    print("4. Search events")
    print("5. Quit\n")
    return input("Enter your choice(1-5): ").strip()


def main():
    print("=================================================")
    print("= Sydney Yummy Catering Event Management System =")
    print("=(c) Developed by Md Aminul Islam (ID: 12312185)=")
    print("=================================================")

    manager = EventManager()

    while True:
        choice = show_menu()

        if choice == "1":
            name = get_non_empty("Enter event name: ")
            date = get_non_empty("Enter event date (yyyy-mm-dd): ")
            while not validate_date(date):
                print("Invalid date. Please enter a valid date in yyyy-mm-dd format.")
                date = get_non_empty("Enter event date (yyyy-mm-dd): ")
            location = get_non_empty("Enter event location: ")
            guests = get_positive_int("Enter number of guests (5-500): ")
            manager.add_event(name, date, location, guests)

        elif choice == "2":
            manager.display_events()

        elif choice == "3":
            manager.save_events()

        elif choice == "4":
            keyword = get_non_empty("Enter search keyword: ")
            manager.search_events(keyword)

        elif choice == "5":
            print(
                "\nGoodbye! Thank you for using the Sydney Yummy Catering Event Management System.\n"
                "In case you want to see the events again, just run the program and they will be loaded from the file.\n"
                "Remember to save your events before quitting to ensure they are stored for next time.\n"
                "See you next time! Have a great day!\n"
                "======================================================================================================\n")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


#  Run the program
if __name__ == "__main__":
    main()
