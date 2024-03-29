#!/usr/bin/python3
"""Module performs log parsing"""
import sys


def print_message(dic_sc, total_file):
    """ Method prints the message
    Args:
        dic_sc: dict of status codes
        total_file: is the total number of the files
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file))
    for k, v in sorted(dic_sc.items()):
        if v != 0:
            print("{}: {}".format(k, v))

total_file = 0
s_code = 0
counter = 0
dic_sc = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # trimming line
        parsed_line = parsed_line[::-1]  # inverting line

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file += int(parsed_line[0])  # file size line
                s_code = parsed_line[1]  # status code line

                if (s_code in dic_sc.keys()):
                    dic_sc[s_code] += 1

            if (counter == 10):
                print_message(dic_sc, total_file)
                counter = 0

finally:
    print_message(dic_sc, total_file)
