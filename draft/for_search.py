import time

peoples_list = ['Harry Styles agent', 'Harry Styles manager', 'Harry Styles publicist',
                'Jack Harlow agent', 'Jack Harlow manager', 'Jack Harlow publicist',
                'Lil Baby agent', 'Lil Baby manager', 'Lil Baby publicist',
                'Post Malone agent', 'Post Malone manager', 'Post Malone publicist',
                'Lizzo agent', 'Lizzo agent', 'Lizzo publicist',
                'Luke Combs agent', 'Luke Combs manager', 'Luke Combs publicist',
                'Carrie Underwood agent', 'Carrie Underwood manager', 'Carrie Underwood publicist',]

list_for_search = []

for item in peoples_list:
    list_for_search.append((item.replace(' ', '+'), item.replace(' ', '_')))
    # 0 это для поиска / 1 будет для названия файла


import datetime

start_date = datetime.date(2022, 5, 17)
end_date = datetime.date(2022, 5, 10)
delta = datetime.timedelta(days=1)

# while start_date > end_date:
#     print(start_date.month, start_date.day)
#     start_date -= delta
#
# print(list_for_search)
# for item in list_for_search:
#     print(item[1])
#     print(item[0])
#     time.sleep(2)