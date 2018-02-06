#!/usr/bin/env python
#-*- coding: utf-8 -*-
#__author__ = "Sunny Arora"
#__license__ = "MIT"

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import json


months_dict = ((1, "January"), (2, "February") ,(3, "March"),
                (4, "April"), (5, "May"), (6, "June"),
                (7, "July"), (8, "August"), (9, "September"),
                (10, "October"), (11, "November"), (12, "December"))


class IndianFestivals(object):
    """
    Get all Major Festivals celebrated as per Indian calendar
    on yearly and monthly basis in json prettyprint format
    """

    def __init__(self, year):
        # Parse below url to get all festivals and holidays info
        page = urlopen("https://panchang-1205.appspot.com/calendars/indiancalendar?date=%s&lid=1261481&language=en"% year)
        soup = BeautifulSoup(page, 'html.parser')
        self.festivals = soup.findChildren('table')

    def get_festivals_in_a_year(self, month=None):
        """
        Festivals celebrated in a particular year

        Optional Arguments:

        month: Calendar month
        type : Integer
        """

        festival_dict = OrderedDict()

        if month:
            month = int(month)
            if month < 1 or month > 12:
                raise Exception("Month should be between 1 and 12")

            fest_month = dict(months_dict)[month]

        festival_dict = OrderedDict()

        for festival in self.festivals:
            # Festival Month
            month_name = festival.findChildren(['thead'])[0].findChildren("th")[0].text.split(" ")[0]

            if month and not fest_month == month_name:
                continue

            # All festivals in a month
            festival_details_per_month = festival.findChildren(['tbody'])[0].findChildren("tr")
            festival_dict[month_name] = []

            # Store day, date and name for each festival
            for festival_detail in festival_details_per_month:
                fests = festival_detail.findChildren("td")
                festival_dict[month_name].append(
                    {"date": fests[0].text.strip().split(" ")[0],
                        "day": fests[0].text.strip().split(" ")[1],
                            "name": fests[1].text.strip()})

            if month:
                return json.dumps(festival_dict[fest_month], indent=1)

        return json.dumps(festival_dict, indent=1)

    def get_festivals_in_a_month(self, month):
        """
        Festivals celebrated in a particular month of a year

        Arguments:

        month: Calendar month
        type : Integer
        """

        return self.get_festivals_in_a_year(month)

    def get_religious_festivals_in_a_year(self, month=None):
        """
        Festivals celebrated as per different religions
        in a particular year

        Optional Arguments:

        month: Calendar month
        type : Integer
        """

        festival_dict = OrderedDict()

        if month:
            month = int(month)
            if month < 1 or month > 12:
                raise Exception("Month should be between 1 and 12")

            fest_month = dict(months_dict)[month]

        festival_dict = OrderedDict()

        for festival in self.festivals:

            # All festivals in a month
            festival_details_per_month = festival.findChildren(['tbody'])[0].findChildren("tr")

            # Store day, date and name for each festival
            for festival_detail in festival_details_per_month:
                # Festival Month
                month_name = festival.findChildren(['thead'])[0].findChildren("th")[0].text.split(" ")[0]

                fests = festival_detail.findChildren("td")
                bold_tags = fests[1].findChildren("b")
                link_tags = fests[1].findChildren("a")

                if bold_tags:
                    for tag in bold_tags:
                        if tag.get("style") and tag.get("style")[0] is not None:
                            color = tag.get("style").split(":")[1]

                            festival_type = self.get_fest_type(color)
                            festival_name = tag

                            if festival_type not in list(festival_dict.keys()):
                                festival_dict[festival_type] = []

                            if month and not fest_month == month_name:
                                continue

                            festival_dict[festival_type].append(
                                {"date": fests[0].text.strip().split(" ")[0],
                                    "day": fests[0].text.strip().split(" ")[1],
                                    "month": month_name,
                                        "name": festival_name.text.strip()})

                if link_tags:
                    for tag in link_tags:
                        if tag.get("style") and tag.get("style")[0] is not None:
                            color = tag.get("style").split(":")[1]

                            festival_type =  self.get_fest_type(color)
                            festival_name = tag

                            if festival_type not in list(festival_dict.keys()):
                                festival_dict[festival_type] = []

                            if month and not fest_month == month_name:
                                continue

                            festival_dict[festival_type].append(
                                {"date": fests[0].text.strip().split(" ")[0],
                                    "day": fests[0].text.strip().split(" ")[1],
                                    "month": month_name,
                                        "name": festival_name.text.strip()})

        return json.dumps(festival_dict, indent=1)

    def get_religious_festivals_in_a_month(self, month):
        """
        Festivals celebrated as per different religions
        in a particular month of a year

        Arguments:

        month: Calendar month
        type : Integer
        """

        return self.get_religious_festivals_in_a_year(month)

    def get_fest_type(self, color):
        festival_type = None

        if color == "#a60000":
            festival_type = "Hindu Festivals"
        elif color == "#4A3475":
            festival_type = "Goverment Holidays"
        elif color == "#556A21":
            festival_type = "Sikh Festivals"
        elif color == "#d42426":
            festival_type = "Christian Holidays"

        return festival_type


if __name__ == "__main__":
    # Sample Test Code
    year = "2018"
    month = 2
    fest = IndianFestivals(year)

    all_fests=fest.get_festivals_in_a_year()
    fests_month=fest.get_festivals_in_a_month(month)
    all_religious_fests=fest.get_religious_festivals_in_a_year()
    fests_religious_month=fest.get_religious_festivals_in_a_month(month)

    print("Festivals in year %s : " % year)
    print(all_fests)
    print("================================================")
    print("Festivals in month %s for year %s: " %
        (dict(months_dict)[month], year))
    print(fests_month)
    print("================================================")
    print("Religious Festivals in year %s : " % year)
    print(all_religious_fests)
    print("================================================")
    print("Religious Festivals in month %s for year %s: " %
        (dict(months_dict)[month], year))
    print(fests_religious_month)