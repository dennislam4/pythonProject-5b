# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-18-2022
# Description: Allows the user to search JSON file data on Nobel Prizes.

import json


class NobelData:
    """Represents Nobel Prize data."""

    def __init__(self):
        with open('nobels.json', 'r') as infile:
            self._nobel_data = json.load(infile)

    def search_nobel(self, year, catagory):
        """
        Search method for NobelData. Returns a sorted list of the surnames for the winner(s) for each searched catagory
        and year.
        """
        winners = []

        for index in self._nobel_data["prizes"]:
            prize_year = index["year"]
            prize_catagory = index["category"]

            if prize_year == year and prize_catagory == catagory:
                for l_list in index["laureates"]:
                    winners.append(l_list["surname"])
        winners.sort()
        return winners



