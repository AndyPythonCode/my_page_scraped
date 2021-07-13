# from scraping.scraper import PageSources
from bs4 import BeautifulSoup
import csv

# Testing my own module
# page = PageSources('https://andycode.ga')
# page.get_current_html()
# page.save()

PAGE_FILE = './web_data/andycode_1.html'
PAGE_HTML: str

with open(PAGE_FILE, 'r') as html:
    PAGE_HTML = html.read()
    html.close()

soup = BeautifulSoup(PAGE_HTML, 'lxml')

dict_data = list()
csv_columns = ['From','To','Abbreviation','Place', 'Course','Logo']

sectionStudy = soup.find(id='Study')

studies = sectionStudy.find_all('div', {'class': 'py-8 lg:w-1/3'})

for study in studies:
    header = study.find('div', {'class': 'w-12 flex-shrink-0 flex flex-col text-center leading-none'})
    body = study.find('div', {'class': 'flex-grow pl-6'})

    dict_data.append(
        {
            'From':         list(header)[0].string,
            'To':           list(header)[-1].string,
            'Abbreviation': body.h2.string,
            'Place':        body.h1.string,
            'Course':       body.p.string,
            'Logo':         body.a.img["src"]
        })

csv_file = "andycode.csv"

try:
    with open(csv_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except ValueError as e:
    print(f'Fix it, and run again: {e}')
finally:
    print('\nFinished...')