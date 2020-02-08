#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(
                    error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)

"""Create an output file
Let's define another function file_output that takes returned_errors, returned by a previous function, as a formal parameter.

def file_output(returned_errors):

Using Python file handling methods, write returned_errors into the errors_found.log file by opening the file in writing mode. For defining the output file, we'll use the method os.path.expanduser ('~'), which returns the home directory of your system instance. Then, we'll concatenate this path (to the home directory) to the file errors_found.log in /data directory.

  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:

Next, write all the logs to the output file by iterating over returned_errors.

    for error in returned_errors:
      file.write(error)

And finally, close the file.

    file.close()

Function call
Now, let's call the functions and run the script.

Define the main function and call both functions that we defined in the earlier sections.

The variable log_file takes in the path to the log file passed as a parameter. In our case, the file is fishy.log. Call the first function i.e., error_search() and pass the variable log_file to the function. This function will search and return a list of errors that would be stored in the variable returned_errors. Call the second function file_output and pass the variable returned_errors as a parameter.

sys.exit(0) is used to exit from Python, the optional argument passed can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered "successful termination" and any nonzero value is considered an "abnormal termination" by shells.
This script will now prompt for the type of error to be searched. Continue by entering the following type of error:

CRON ERROR Failed to start

On successful execution, this will generate an errors_found.log file, where you will find all the ERROR logs based on your search. You can view the ERROR log using the command below:
"""
