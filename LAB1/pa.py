from gmail import GMail, Message
from random import choice

content_template='''
<p>Dear <span style="color: #ff0000;"><em><strong>Hellen</strong></em></span>,</p>
<p>It is such an honor for us to have you participate our {{program}}</p>
<p>hope to meet you soon !</p>'''

program_list=["program","summit","event"]
program=choice(program_list)

content1=content_template.replace("{{program}}","summit")

gmail=GMail("queenslandcfa1990@gmail.com", "princeton1990")
msg=Message("Say Hi", to="queensland1990@gmail.com", html=content1)
gmail.send(msg)
