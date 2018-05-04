from urllib.request import urlopen # call url library, specifically a part of this library
from bs4 import BeautifulSoup
url="http://dantri.com.vn"
## step 1
#1.1 open a connection btw my computer and the link above
conn=urlopen(url)


#1.2 read database --> we have raw material
raw_data=conn.read()


#1.3 decode data  (exp we notify that data is text document, not film, all are from urllib)
text=raw_data.decode('utf8')

# print(text)

#2. save file
#2.1 open connection
# dan_tri_file=open("dantri.html","wb") # luu text thi "w", luu raw_data thi dung wb (write binary)
# #2.2  write
# dan_tri_file.write(raw_data)
# #2.3 close connection
# dan_tri_file.close()

# step 2: find roi
soup=BeautifulSoup(text,"html.parser")
# print(soup.html)

ul=soup.find("ul","section-content","section chart-grid")
#print(ul.prettify())

li_list=ul.find_all("li")
#print(li_list.prettify())
item_list=[]
for li in li_list:
# li=li_list[0]
# print(li.prettify())
    a=li.h4.a
    # print(a.prettify())
    title=a.string #string or content
    # print(title)
    link=url+a["href"]
    item={
        "Title":title,
        "Link": link
    }
    item_list.append(item)

    # print(item)
    # print('*******')
    # print(title)
    # print(link)
    # print("-------------------")
# print(item_list)
import pyexcel
pyexcel.save_as(records=item_list, dest_file_name="dantri.xlsx")
