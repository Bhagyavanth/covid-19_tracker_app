import requests
from bs4 import BeautifulSoup


# web scraping



def get_dic(country_name):
    """ get the cases of the selected country"""
    return dic[country_name]

dic={}
def webScraping():
    url='https://www.worldometers.info/coronavirus/'

    html_page = requests.get(url).text

    soup=BeautifulSoup(html_page,'html.parser')
    get_table=soup.find('table',id='main_table_countries_today')
    get_table_data=get_table.tbody.find_all('tr')


    for i in range(8,len(get_table_data)):
        try:
            key=get_table_data[i].find_all("a", href=True)[0].string
        except:
            key=get_table_data[i].find_all('td')[0].string

        values=[j.string for j in get_table_data[i].find_all('td')]

        dic[key]=values[2:9]

