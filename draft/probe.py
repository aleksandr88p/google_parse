from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import time
import datetime
import random
import csv
from for_search import list_for_search

"""
диапазон даты в конце линки
min%3A5%2F11%2F2022%2Ccd_max%3A5%2F11%2F2022&tbm это значит от 11 мая 2022 до 11 мая 2022
min%3A3%2F17%2F2022%2Ccd_max%3A3%2F17%2F2022&tbm

https://www.google.com/search?q=trump&lr=lang_en&cr=countryUS&safe=images&as_qdr=all&source=lnt&tbs=lr%3Alang_1en%2Cctr%3AcountryUS%2Ccdr%3A1%2Ccd_min%3A3%2F17%2F2022%2Ccd_max%3A3%2F17%2F2022&tbm=
https://www.google.com/search?q=trump&lr=lang_en&cr=countryUS&safe=images&as_qdr=all&source=lnt&tbs=lr%3Alang_1en%2Cctr%3AcountryUS%2Ccdr%3A1%2Ccd_min%3A4%2F22%2F2022%2Ccd_max%3A4%2F22%2F2022&tbm=
"""

def google_search(link, date):
    print('func start')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }

    # proxies = {
    #     'https': 'http://1xe71qbv:1doac1s8@92.255.253.185:16548'
    # }

    # print('response start')
    # response = requests.get(url=link, headers=headers, proxies=proxies)
    date = date
    # print(date)
    # print(link)
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    # print(webpage)
    # time.sleep(random.randint(1, 3))
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        # print(soup)
        """ 
        пройдемся в цикле по супу и используем метод find_all
        передадим туда атрибуты (какой тег ищем и его атрибуты)
        класс я нахожу со ссылкок в супе 
        """
        # 'div', class_='egMi0 kCrYT' или 'ZINbbc luh4tb xpd O9g5cc uUPGi'
        for item in soup.find_all('div', attrs={'class':'ZINbbc luh4tb xpd O9g5cc uUPGi'}):
            title = ''
            descrip = ''
            dat = ''
            link = ''
            raw_link = (item.find('a', href=True)['href'])
            link = (raw_link.split("/url?q=")[1]).split("&sa")[0]
            title = (item.find('div', attrs={'class':'BNeawe vvjwJb AP7Wnd'})).get_text()
            description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})).get_text()
            if ' · ' in description:
                description = description.split(' · ')
                descrip = description[1]
                dat = description[0]
            else:
                descrip = description
            title = title.replace(',', '')
            print(title)
            print(descrip)
            descrip = descrip.replace(',', '')
            # print(dat)
            print(link)
            # print(description)
            print("*************")
            # print(item)
            # document = open(f'data.csv', 'a')
            # document.write("{}, {}, {} \n".format(title, descrip, link)) # запись в файл с запятыми как разделитель
            # document.close()
            writer.writerow((title, descrip, link, date))

        """теперь нужно сделать возможность нажимать кнопку next"""
        next_link = soup.find('a', attrs={"aria-label":"Next page"})['href']
        sec_to_sleep = random.randint(5, 10)
        time.sleep(sec_to_sleep)
        google_search(root+next_link, date)

# link = f"https://www.google.com/search?q={who}&lr=lang_en&cr=countryUS&hl=en&source=lnt&tbs=lr%3Alang_1en%2Cctr%3AcountryUS%2Ccdr%3A1%2Ccd_min%3A{month_from}%2F{day_from}%2F2022%2Ccd_max%3A{month_to}%2F{day_to}%2F2022&tbm="


for item in list_for_search:
    csv_file = open(f'{item[1]}.csv', 'w+')
    writer = csv.writer(csv_file)
    root = "https://www.google.com/"
    who = None
    start_date = datetime.date(2022, 5, 17)
    end_date = datetime.date(2022, 5, 11)
    delta = datetime.timedelta(days=1)
    while start_date > end_date:
        # print(start_date.month, start_date.day)
        who = item[0]
        month_from = start_date.month
        day_from = start_date.day
        month_to = start_date.month
        day_to = start_date.day
        date = start_date.strftime('%m/%d/%Y')
        print(date)
        link = f"https://www.google.com/search?q={who}&lr=lang_en&cr=countryUS&hl=en&source=lnt&tbs=lr%3Alang_1en%2Cctr%3AcountryUS%2Ccdr%3A1%2Ccd_min%3A{str(month_from)}%2F{str(day_from)}%2F2022%2Ccd_max%3A{str(month_to)}%2F{str(day_to)}%2F2022&tbm="
        print(link)
        try:
            google_search(link, date)
        except Exception as e:
            print("""
    *****************************
    * FINISH  ROUND  WITH  {} {}*
    *****************************""".format(month_from, day_from))

        time.sleep(random.randint(4, 9))
        start_date -= delta

    csv_file.close()
