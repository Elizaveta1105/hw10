import os
import django

from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from quotes.models import Quote, Tag, Author # noqa

client = MongoClient("mongodb+srv://lizamelihovaa:tz8OQrxq2U6fVq59@cluster0.lwq50vv.mongodb.net/")

db = client.hw10

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        tag_obj, _ = Tag.objects.get_or_create(name=tag)
        tags.append(tag_obj)

    is_exist = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not is_exist:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])

        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )

        for tad in tags:
            q.tags.add(tad)
