import re
import operator
import os
import sys

# Regex patterns required for this small project
info_pattern = r"ticky: INFO: ([\w ]*)"
error_pattern = r"ticky: ERROR: ([\w ]*)"
user_pattern = r"\((.*)\)"

line_sample = 'Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)'

# Dictionaries to keep count of each number and user interaction
error = {}
per_user = {}

# A search pattern function that returns a result variable


def search_pattern(pattern, line):
    # return only the captured group
    result = re.findall(pattern, line)
    return result


# Open the syslog.log file. Use for loops to count each occurence of each regex pattern above
# with open(sys.argv[1], 'r') as syslog:
#     for line in syslog.readlines():
#         res_err = search_pattern(error_pattern, line)
#         res_info = search_pattern(info_pattern, line)
#         res_user = search_pattern(user_pattern, line)
#         # Check if the name of the user is already in the per_user dictionary
#         if res_user not in per_user:
#             per_user[res_user] = {'INFO': 0, 'ERROR': 0}
#         # Check if the kind of error is already in the error dictionary
#         elif res_err not in error:
#             error[res_err] = 0
#         # If there is an error
#         elif res_err != []:
#             # increment the value of key 'ERROR' by 1 'INFO' in per_user dictionary
#             per_user[res_user]['ERROR'] += 1
#             # increment the type of that error in the error dictionart
#             error[res_err] += 1
#         # If there is an info string only increment the value of key 'INFO' in per_user dictionary
#         elif res_info != []:
#             per_user[res_user]['INFO'] += 1
#     syslog.close()

# sort the dictonaries

error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items(), key=operator.itemgetter(0))
print(error)
