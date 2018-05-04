from urllib.request import urlopen
from bs4 import BeautifulSoup
url='http://dantri.com.vn/'
conn=urlopen(url)
raw_data=conn.read()
text=raw_data.decode('utf8')
#print(text)
# pa_file=open("kenh14.html","wb")
# pa_file.write(raw_data)
# pa_file.close()
# find roi
soup=BeautifulSoup(text,"html.parser")
# print(soup.prettify())
ul=soup.find("ul","ul1 ulnew")
# print(ul.prettify())
li_list=ul.find_all("li")
item_list=[]
for li in li_list:
    a=li.h4.a
    title=a.string
    link=url+a['href']
    item={
        "title": title,
        "Link": link
    }
    item_list.append(item)
print(item_list)
import pyexcel
pyexcel.save_as(records=item_list, dest_file_name="palink.xlsx")
    # print(item)
    # print('-------------------------')
# # print(title)
# # print(a.prettify())
# import pyexcel
# data=[
#     {
#         "name":"Huyen",
#         "age":23
#     },
#     {
#         "name":"Hellen",
#         "age":24
#     },
#     {
#         "name": "An",
#         "age":25
#     }
# ]
# pyexcel.save_as(records=data,dest_file_name="data1.xlsx")
