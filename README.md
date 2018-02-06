# Indian Festivals

API to provide all festivals celebrated in India on yearly and monthly basis.
Also gives festivals celebrated as per different people of the society.

## Features

- Festivals celebrated in India in a particular year.
- Festivals celebrated in India in a particular month of a year.
- Festivals celebrated in India by people of different society in a particular year.
- Festivals celebrated in India by people of different society in a particular month of a year.

## Requirements

- Python >=2.7
- BeautifulSoup

## Installation

You can install from PyPI. Just do :

    $ pip install indian_festivals

## How to Use

- Dummy year and month

year = "2018", month = "1"

Import Library :

    $ from indian_festivals import IndianFestivals
    
Create a new instance with the year for which the list of festivals is required :

    $ fest = IndianFestivals(year)

Get festivals for a particular year :

    $ fest.get_festivals_in_a_year()
    
Get festivals for a particular month in a year :

    $ fest.get_festivals_in_a_month(month)

Get festivals for a particular year as per different religions :

    $ fest.get_religious_festivals_in_a_year()
    
Get festivals for a particular month in a year as per different religions :

    $ fest.get_religious_festivals_in_a_month(month)
