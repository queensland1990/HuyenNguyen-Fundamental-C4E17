from pymongo import MongoClient

#1. connect database
uri="mongodb://queensland1990:Princeton1990@ds163294.mlab.com:63294/c4e17"
client=MongoClient(uri)

#2. get default database
db=client.get_default_database()

#3. get blog collection
blog=db["blog"]

#4. write a new blog
post= {
    "title": "today, it is rainy",
    "content": "I just want to sleep on my bed"
}

#blog.insert_one(post)
all_posts=blog.find()
for post in all_posts:
    print(post)
