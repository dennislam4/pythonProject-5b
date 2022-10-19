# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-18-2022
# Description: Allows the user to search JSON file data on Nobel Prizes.

import json


class NobelData:
    """Represents Nobel Prize data."""

    def __init__(self):
        with open('nobels.json', 'r') as infile:
            self.nobel_data = json.load(infile)

    def search_nobel(self, year, catagory):
        """
        Search method for NobelData. Returns a sorted list of the surnames for the winner(s) for each searched catagory
        and year.
        """
        winners = []
        surnames_of_winners = []

        for index in range(0, len(self.nobel_data["prizes"])):
            prize_year = self.nobel_data["prizes"][index]["year"]
            prize_catagory = self.nobel_data["prizes"][index]["catagory"]

            if prize_year == year and prize_catagory == catagory:
                winners = (self.nobel_data["prizes"][index]["laureates"])
            pass

        for index in range(0, len(self.nobel_data["winners"])):
            surnames_of_winners.append(winners[index]["surname"])
        return surnames_of_winners.sort()

