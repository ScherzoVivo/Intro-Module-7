# Assignment 7 Documentation

## Introduction:
In this assignment we’re going to look at structured error handling by building an address book script. The basic principle is that the user will input address information and if anything is an incorrect format, the program will return an error, but still resume main loop operation.

## Section 1: Import and Variables
To begin, lines 13-16 import necessary modules. The 3rd party module pandas is required as denoted in the requirements.txt document. (Thank you, Sophia! 😊) 

Establishing the script variables on lines 18 through 26 is simply a matter of pre-defining the master_data list that will contain all loaded and added dictionary records as well as the list of states used to validate content entry further down.

## Section 2: Custom Exceptions and Error Handling
Progressing down to the two custom Exception classes for the script, they’re designed to overwrite the currently existing Python error handlers and instead provide my specified feedback (specified in the __str__ method) in the event an error is thrown. (Figure 1)
```
28	class FileEXTError(Exception):
29	    """File extension must be .dat for successful parsing."""
30	####################
31	    def __str__(self):
32	        return "Invalid file extension."
```
> Figure 1. Custom exception class designed to catch incorrect file extensions.)

The second portion of this section consists of a simple expression that displays a cleaner, stylized alternative to the default error handling protocol. Lines 40-53 just outline a group of print statements that return the function’s above-mentioned __str__ value. (Figure 2)

```
33	print("\n==============================")
34	print("There was an error! Oopsie!\n")
35	print(error.__doc__)
36	print("==============================\n")
```
> Figure 2. Custom error message

## Section 3: Loading File Data

The next section, lines 55-82, defines the load_data function, which calls for two parameters (the master_data object previously initialized – for storing the file contents actively in memory – and the filename specified by the user further down in the main loop.

The following bit of script on lines 68-73 runs a test to ensure the file is of the correct type (.dat), and if not use the throw_error function from previously to display one of the initially-defined custom Exception classes – in this case the FileEXTError.

Following this, lines 76-82 run a simple load function and passes the object into the pickle module for conversion from binary data into the regular Python dictionaries. Then we simply run a small for loop to put the unpacked dictionaries into the master_data list, which it returns for manipulation.

## Section 4: Adding Records

In lines 84-175 we request desired input from the user, ensure formatting is correct, and add to the working master_data before returning it into the loop. It accepts two parameters – the master_data list object, and the record_count variable, which acts as a counter for which ID number the new record will be assigned.

Below the docstring and initial print statements, on line 100-106, is a series of initial input statements intended to capture (and format) the different address components. Note that depending on the type of component, the formatting methods applied are different – title() or upper().

Lines 109-130 deal primarily with data validation. Using a pair of try/except blocks in conjunction with series of if statements to accomplish then following (Figure 3):

```
37	try:
38	    if len(phone) != 10:
39	        print("Phone number must be 10 numbers (with no spaces/separators).")
40	        raise ValueError()
41	    if not phone.isnumeric():
42	        print("Phone number must be numeric and contain only 9 digits.")
43	        raise ValueError()
44	    if len(state) != 2:
45	        print("State input should be the two-letter abbreviation. Please try again.")
46	        raise ValueError()
47	    if state not in states:
48	        print("You must enter a valid state abbreviations. Please try again.")
49	        raise ValueError()
50	    if len(zipcode) != 5:
51	        print("Postal code should be five digits. Please try again.")
52	        raise ValueError()
53	    if not zipcode.isnumeric():
54	        print("Postal code should only consist of numbers. Please try again.")
55	        raise ValueError()
56	except Exception as x:
57	    throw_error(x)
58	    return
```
> Figure 3. Data validation

In the event any of these conditions are not met, an exception is raised and the error is handled on lines 128-130 (as within the load_data function).

Lines 134-153 are a stylized way of confirming the user’s input. The obtained data is printed to the screen and the user is asked to approve. If they type “y” or “yes”, the data is bundled into a dictionary object in lines 155-164 before being added to the working master_data list on line 166, which is then returned at the end of the function.

## Section 5: Removing Records
The function that allows a user to remove records from the data is fairly simple, and this is where the ID number of the record is important. The logic being that the user will have a far easier time inputting small number as opposed to typing in a full task name to indicate what should be removed. This method cycles through all records, starting on line 186, and if it finds an ID number matching the one entered by the user (on line 184), the script displays a formatted single datafame record (the record appears looking tidy and easy to read with minimal code, which is one of the reasons I’ve opted to use the Pandas module in this script).

If the user confirms the action, the pop method is run on line 199 to remove the record from the master_data list, which is then returned into the main loop.

## Section 6: Saving Data
The save_data function operates in a nearly identical way to the load_data function defined above. As before, it confirms that the filename entered by the user has to correct extension before using the Pickle module to pack the master_data list object into a binary file. It then asks if the user would like to exit, terminating the script if the user confirms.

## Section 7: Main Loop
The final block of code, comprised of lines 244-289, is the primary loop for the function. Before actually entering into the loop, the script runs the load_data function described above to pull any current data from the applicable file. To initialize the loop I set the running variable to True and use it in a while loop. The first step of each loop iteration is to display the main menu, written in a print statement over multiple lines.

Following the menu is a brief try/except block that validates the user’s menu choice, raising a ValueError and returning to the beginning of the loop if something other than one of the menu option numbers is entered. 

The final chunk of code is the event handler determining which process to run based on the user input. The only thing different here is the code for option #3 – View Records (lines 283-285)– which simply formats the current working data into a pretty pandas data frame before printing it to the screen. I opted to avoid a function for this since the code was only two lines and the docstring would end up being longer than the function itself! Note that in order to avoid displaying the data frame’s numerical record index (which may differ from the assigned ID number), we use the “index=False” argument in the to_string method.
