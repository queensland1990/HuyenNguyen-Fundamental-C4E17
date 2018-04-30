from gmail import GMail, Message
import datetime
now=datetime.datetime.now()

html_template='''
<p>Dear Anh<span style="color: #ff0000;"><strong> Huy</strong></span></p>
<p>Hom nay ngu day, di kham bi {{sickness}}, em xin nghi phep, khong e lay {{sickness}} cho thay day ah</p>
<p>Hoc tro yeu quy.</p>'''

from random import choice
sickness_list=["Kiet ly","thuong han","sot ret"]
sickness=choice(sickness_list)

html_content=html_template.replace("{{sickness}}",sickness)
mail=GMail("queenslandcfa1990@gmail.com","princeton1990")
msg=Message("Im_sick", to='queensland1990@gmail.com', html=html_content)
if now.hour>7:
    mail.send(msg)
