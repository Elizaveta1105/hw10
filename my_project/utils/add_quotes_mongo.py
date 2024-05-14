import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb+srv://lizamelihovaa:tz8OQrxq2U6fVq59@cluster0.lwq50vv.mongodb.net/")

db = client.hw10

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)


for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })