from mongoengine import connect
import json
from models import *


def load_authors_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author(**author_data)
            author.save()


def load_quotes_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data.pop("author")
            author = Author.objects(fullname=author_name).first()
            if author:
                quote_data["author"] = author
                quote = Quote(**quote_data)
                quote.save()


uri = "mongodb+srv://zhowtenkooleksiy:OdqjdrrgrJDD64qf@db-hw2-08.u8lqztr.mongodb.net/?retryWrites=true&w=majority"

connect(
    db="hw2_09db",
    host=uri,
)

autors = "authors.json"
quotes = "quotes.json"

try:
    load_authors_from_json(autors)
    load_quotes_from_json(quotes)
    print("Вы успешно подключились к MongoDB и загрузили авторов и их цитаты")
except Exception as e:
    print(e)
