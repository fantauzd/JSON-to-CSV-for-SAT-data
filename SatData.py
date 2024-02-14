# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/31/2023
# Description: Defines a class that reads sat data from a JSON file. The class contains a save_as_csv method
# to take a list of dbns (codes) and return a formated csv file of relevant test score data for each code

import json

def sort_list(list_dbn):
    """
    Receives a list and returns a sorted version of same list. Uses insertion sort.
    :param list_dbn: a list
    :return: A sorted version of the passed list
    """
    for element in range(1, len(list_dbn)):
        val = list_dbn[element]
        pos = element - 1
        while pos >= 0 and list_dbn[pos] > val:
            list_dbn[pos + 1] = list_dbn[pos]
            pos -= 1
        list_dbn[pos + 1] = val


class SatData:
    """
    Reads a JSON file containing data on 2010 SAT results for New York City
    and writes the data to a text file in CSV format.
    """

    def __init__(self):
        with open('sat.json', 'r') as infile:
            self._data = json.load(infile)["data"]  # accesses the list of lists at line 667 of sat.json


    def save_as_csv(self, list_dbn):
        """
        Takes as a parameter a list of DBNs (district bureau numbers) and saves a CSV file that lists the
        DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean in order ( seperated
        by commas).
        :param list_dbn: list of dbns
        :return: a csv file where the rows represent the dbns and there are columns for the name, number of test takers,
        and scores
        """
        first_line = ['DBN','School Name','Number of Test Takers','Critical Reading Mean','Mathematics Mean','Writing Mean']
        next_lines = []  # initializes lines to be added to csv
        with open('output.csv', 'w') as outfile:
            outfile.write(','.join(first_line) + '\n')  # hardcodes the first line of the csv
            for school in self._data:
                if school[8] in list_dbn:  # the dbn is always the 8 value in the list for each school
                    line = []  # initializes line for each dbn we find
                    # There are 5 columns we want to grab, starting at index 8 and ending at index 13
                    for element in range(6):
                        val = school[8 + element]
                        if val is not None and ',' in val:  # checking for ',' in value does not work with NoneType
                            val = '"' + val + '"'
                        line.append(val)  # builds new line to write
                    next_lines.append(line)  # saves all lines to be written in one list
            sort_list(next_lines)  # sorts list
            for line in next_lines:
                outfile.write(','.join(line) + '\n')
