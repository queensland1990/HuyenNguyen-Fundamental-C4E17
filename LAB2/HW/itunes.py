from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.apple.com/itunes/charts/songs'
conn=urlopen(url)
raw_data=conn.read()
text=raw_data.decode('utf8')
soup=BeautifulSoup(text,"html.parser")
ul=soup.find('section', 'section chart-grid')
li_list=ul.find_all("li")
item_list=[]
for li in li_list:
    a=li.h3.a
    b=li.h4.a
    song_name=a.string
    artist=b.string
    item={
        "Song_names":song_name,
        "Artist":artist
    }
    item_list.append(item)

import pyexcel
pyexcel.save_as(records=item_list,dest_file_name="itunes100.xlsx")

from youtube_dl import YoutubeDL
for song in item_list:
    options={
        'default_search':'ytsearch',
        'max_dowloads': 1,
        'format': :'bestaudio/audio'
    }
    dl=YoutubeDL(options)
    dl.download([song_name])
