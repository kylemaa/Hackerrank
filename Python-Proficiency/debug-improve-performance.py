#!/usr/bin/env python3
import csv
import datetime
import requests
import operator

FILE_URL = "http://marga.com.ar/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    # Decode all lines into strings
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_same_or_newer(start_date, data):
    """Returns the employees that started on the given date, or the closest one$"""
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in sorted(reader, key=operator.itemgetter(3)):
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        # Get the other half of the sorted array if row date is equal or greater than start date
        if row_date >= start_date:
            if row_date < min_date:
                min_date = row_date
                min_date_employees = []
            if row_date == min_date:
                min_date_employees.append("{} {}".format(row[0], row[1]))
    return min_date, min_date_employees


def list_newer(start_date, data):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date, data)
        print("Started on {}: {}".format(
            start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)


def main():
    start_date = get_start_date()
    data = get_file_lines(FILE_URL)
    list_newer(start_date, data)


if __name__ == "__main__":
    main()
