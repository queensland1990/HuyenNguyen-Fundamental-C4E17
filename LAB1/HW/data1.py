from pymongo import MongoClient
client=MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db=client.get_default_database()
