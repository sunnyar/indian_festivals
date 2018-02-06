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
    
    Sample o/p :
    {
     "January": [
      {
       "day": "Monday",
       "date": "1",
       "name": "New Year"
      },
      {
       "day": "Saturday",
       "date": "13",
       "name": "Lohri"
      },
      {
       "day": "Friday",
       "date": "26",
       "name": "Republic Day"
      }
     ],
     "February": [
      {
       "day": "Tuesday",
       "date": "13",
       "name": "Mahashivratri"
      }
     ]
     ....
    }
    
Get festivals for a particular month in a year :

    $ fest.get_festivals_in_a_month(month)
    
    Sample o/p :
    [
     {
      "date": "13",
      "name": "Mahashivratri",
      "day": "Tuesday"
     }
    ]

Get festivals for a particular year as per different religions :

    $ fest.get_religious_festivals_in_a_year()
    
    Sample o/p :
    
    {
     "Christian Holidays": [
      {
       "date": "1", 
       "day": "Monday", 
       "name": "New Year", 
       "month": "January"
      }, 
      {
       "date": "25", 
       "day": "Tuesday", 
       "name": "Merry Christmas", 
       "month": "December"
      }
     ], 
     "Sikh Festivals": [
      {
       "date": "13", 
       "day": "Saturday", 
       "name": "Lohri", 
       "month": "January"
      }, 
      {
       "date": "14", 
       "day": "Saturday", 
       "name": "Baisakhi", 
       "month": "April"
      }
     ], 
     "Hindu Festivals": [
      {
       "date": "14", 
       "day": "Sunday", 
       "name": "Makar Sankranti", 
       "month": "January"
      }, 
      {
       "date": "14", 
       "day": "Sunday", 
       "name": "Pongal", 
       "month": "January"
      }, 
      {
       "date": "14", 
       "day": "Sunday", 
       "name": "Uttarayan", 
       "month": "January"
      }
      ]
    }

Get festivals for a particular month in a year as per different religions :

    $ fest.get_religious_festivals_in_a_month(month)
    
    Sample o/p :
    
    {
     "Christian Holidays": [], 
     "Sikh Festivals": [], 
     "Hindu Festivals": [
      {
       "date": "13", 
       "day": "Tuesday", 
       "name": "Mahashivratri", 
       "month": "February"
      }
     ], 
     "Goverment Holidays": []
    }
