from gmail import GMail, Message

# muon check mail co quan co dung dc ko search python smpt (to check he thong mail co quan co support ko )
html_template='''
<p>Dear Ms<span style="color: #ff0000;"><strong> Betsy</strong></span></p>
<p>Hom nay ngu day, di kham bi {{sickness}}, em xin nghi viec, khong e lay {{sickness}} cho sep day</p>
<p>Nhan vien yeu quy.</p>'''

from random import choice
sickness_list=["Kiet ly","dau bung"]
sickness=choice(sickness_list)

html_content=html_template.replace("{{sickness}}",sickness)
mail=GMail("queenslandcfa1990@gmail.com","princeton1990")
msg=Message("Say hi", to='queensland1990@gmail.com', html=html_content)
mail.send(msg)
