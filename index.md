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
