######################################################################
# Address Validation Script -- address.py --
# C:\Users\Alleg\Python\UW Course\Week 7\address.py
# Assignment 7 - Structured Error Handling and Pickle
# DJP -- 2021-08-18 -- Designed initial logic and main menu
# DJP -- 2021-08-19 -- Added exception classes, throw_error, remove_record
#                   -- add_record and load_records functions.
# DJP -- 2021-08-20 -- Tidied up main loop, error handling and add_record function.
# DJP -- 2021-08-21 -- Further testing and bug fixes. Added doc strings.
######################################################################
# **Please consult the requirements.txt file before running this script. :)
######################################################################
import pickle
import sys

import pandas   as pd
######################################################################
# Script variables
master_data = []

states = [
"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID",
"IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
"MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
"RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]
######################################################################
class FileEXTError(Exception):
    """File extension must be .dat for successful parsing."""
####################
    def __str__(self):
        return "Invalid file extension."
######################################################################
class ValueError(Exception):
    """Invalid value entered in form."""
####################
    def __str__(self):
        return "Invalid value entered."
######################################################################
def throw_error(error):
    """Error handling message.

    Parameters:
    :error: Exception object

    Returns:
    --Nothing--
    """
####################
    print("\n==============================")
    print("There was an error! Oopsie!\n")
    print(error.__doc__)
    print("==============================\n")
######################################################################
def load_data(master_data):
    """ Reads file and decodes binary data.

    Parameters:
    :master_data: (list) Object to load unpacked data dictionaries into.

    Returns:
    :master_data: (list) Object with unpacked dictionaries loaded in.
    """
####################
    # Input file name and check for proper type
    #fname = input("File name: || ")
    fname = "address.dat"

    try:
        if not fname.endswith(".dat"):
            raise FileEXTError()
    except Exception as x:
        throw_error(x)

    # Open and parse file into memory
    fhandle = open(fname, "rb")
    data = pickle.load(fhandle)

    for i in data:
        master_data.append(i)

    return master_data
######################################################################
def add_record(master_data):
    """Accepts and validates address data input from the user and adds
       to master list in memory.

    Parameters:
    :master_data: (list) object with all current working dictionaries.

    Returns:
    :master_data: (list) object with all current working records including this one.
    """

    print("========================================")
    print("============== ADD RECORD ==============\n")

    # Collect user input
    name = input("Please enter a name: || ").strip().title()
    street = input("Please enter the street number and name: || ").strip().title()
    city = input("Please enter the city: || ").strip().title()
    state = input("Please enter the state (Abbr.): || ").strip().upper()
    zipcode = input("Please enter the 5-digit postal code: || ").strip()
    country = input("Please enter the country (Abbr.): || ").strip().upper()
    phone = input("Please enter the phone number (without spaces): || ").strip()
####################
    # Process input and check for problems
    try:
        if len(phone) != 10:
            print("Phone number must be 10 numbers (with no spaces/separators).")
            raise ValueError()
        if not phone.isnumeric():
            print("Phone number must be numeric and contain only 9 digits.")
            raise ValueError()
        if len(state) != 2:
            print("State input should be the two-letter abbreviation. Please try again.")
            raise ValueError()
        if state not in states:
            print("You must enter a valid state abbreviations. Please try again.")
            raise ValueError()
        if len(zipcode) != 5:
            print("Postal code should be five digits. Please try again.")
            raise ValueError()
        if not zipcode.isnumeric():
            print("Postal code should only consist of numbers. Please try again.")
            raise ValueError()
    except Exception as x:
        throw_error(x)
        return

    phone = f"{phone[0:3]}.{phone[3:6]}.{phone[6:10]}"
####################
    print("\n===============")
    print("Is this correct?\n")
    print(name)
    print(street)
    print(f"{city}, {state} {zipcode}")
    print(phone)
    print("===============")

    correct = input("(Y)es/(N)o || ").lower()
    print("\n")

    if correct in ("n", "no"):
        return

    try:
        if correct not in ("y", "yes"):
            raise ValueError()
    except Exception as x:
        throw_error(x)
        return
####################
    # Set next ID number in sequence
    record_count = master_data[-1]["id"] + 1

    entry = {
        "id" : record_count,
        "name" : name,
        "street" : street,
        "city" : city,
        "state" : state,
        "zip-code" : zipcode,
        "country" : country,
        "phone" : phone
        }

    master_data.append(entry)

    return master_data
######################################################################
def remove_record(master_list):
    """Searches for user-specified ID number and removes record from master list.

    Parameters:
    :master_data: (list) object with all current working dictionaries.

    Returns:
    :master_data: (list) object with all current working records after removing
                  the specified address.
    """

    print("========================================")
    print("============= REMOVE RECORD ============\n")

    remove_id = int(input("Please enter the ID of the record you wish to remove: || "))

    for record, i in enumerate(master_list):
        if i["id"] == remove_id:
            data = i
            df = pd.DataFrame([data], columns = data.keys())

            print("=== Would you like to remove the following record? ===\n")
            print(df.to_string(index=False))
            print("")

            confirm = input("Delete record? (Y)es/(N)o: || ").strip().lower()
            print("")

            if confirm in ("y", "yes"):
                master_list.pop(record)
                return master_list
            else:
                return
######################################################################
def save_data(master_data):
    """Receives current master list in memory and writes it to a binary file.

    Parameters:
    :master_data: (list) object with all current working dictionaries.

    Returns:
    --Nothing--
    """

    filename = input("File name: || ")

    try:
        if not filename.endswith(".dat"):
            raise FileEXTError()
    except Exception as x:
        throw_error(x)

    fhandle = open(filename, "wb")
    pickle.dump(master_data, fhandle)
    fhandle.close

    print("\nData saved successfully!\n")

    exit = input("Would you like to exit?  (Y)es/(N)o || ").lower()

    try:
        if exit in ("y", "yes"):
            print("")
            print("================")
            print("=== Goodbye! ===")
            print("================")
            sys.exit()
        elif exit not in ("n", "no"):
            raise ValueError()
        else:
            print("")
    except Exception as x:
        throw_error(x)
######################################################################
# Load currently existing records from file
load_data(master_data)

# Main loop
running = True
while running:

    print("========================================")

    #Display main menu and get user input
    print("""
    Main Menu:
    1. Add Record
    2. Delete Record
    3. View Records
    4. Save Data
    5. Exit Program

    """)

    try:
        try:
            choice = int(input("Please select an operation. [1 - 5] || "))
        except:
            raise ValueError()
    except Exception as x:
        throw_error(x)
        continue

    print("")

    # Input handling
    if choice == 1:
        add_record(master_data)
    elif choice == 2:
        remove_record(master_data)
    elif choice == 3:
        df = pd.DataFrame(master_data)
        print(df.to_string(index=False))
    elif choice == 4:
        save_data(master_data)
    elif choice == 5:
        sys.exit()
######################################################################
if __name__ == "__main__":
    pass

# address.py
