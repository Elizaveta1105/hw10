from pymongo import MongoClient


def get_mongo_client():
    client = MongoClient("mongodb+srv://lizamelihovaa:tz8OQrxq2U6fVq59@cluster0.lwq50vv.mongodb.net/")
    db = client.hw10

    return db
