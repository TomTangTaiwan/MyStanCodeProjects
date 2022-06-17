"""
File: webcrawler.py
Name: Tom Tang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup

# Constants
YEARS = ['2010s', '2000s', '1990s']

def main():
    for year in YEARS:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #
        tbody = soup.select('tbody > tr')  # Find the table and split each rank to sub-list
        lsts = [tr.text.split() for tr in tbody][:200]  # Remove the table footer from the list

        male_number = sum(int(lst[2].replace(',','')) for lst in lsts)  # Compute total number for male
        female_number = sum([int(lst[4].replace(',','')) for lst in lsts])  # Compute total number for female

        print(f'Male Number: {male_number}')
        print(f'Female Number: {female_number}')

if __name__ == '__main__':
    main()
