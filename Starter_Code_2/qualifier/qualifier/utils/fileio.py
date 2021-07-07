# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


   # @TODO: Complete the usability dialog for savings the CSV Files.

def save_csv(csvpath, qualifying_loans:
    csvpath = Path(qualifying_loans)
    with open(csvpath, 'w') as qualifying_loans:
        csvwriter.writerows(qualifying_loans)
        csvwriter.writeheader(qualifying_loans)


return True