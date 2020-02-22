#!/usr/bin/env python3
import sys
import csv
import os


def process_csv(csv_file):
    """Turn the contents of the CSV file into a list of lists"""
    print("Processing {}".format(csv_file))
    with open(csv_file, "r") as datafile:
        data = list(csv.reader(datafile))
    return data


# def data_to_html(title, data):
#     """Turns a list of lists into an HTML table"""

#     # HTML Headers
#     html_content = """
# <html>
# <head>


# Linux command that gives write permission to the directory that would host that HTML page: sudo chmod  o+w / var/www/html
# navigate to ls / var/www/html
