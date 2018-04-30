from pymongo import MongoClient
uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(uri)

db=client.get_default_database()

posts=db["posts"]

content={
    "title": "Học chơi",
    "author": "queensland1990",
    "content": "Học không chơi đánh rơi tuổi trẻ. Chơi không học vừa khỏe vừa vui"
}
posts.insert_one(content) #(document)
