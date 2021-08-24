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
