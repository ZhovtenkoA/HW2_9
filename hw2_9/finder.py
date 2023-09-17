from models import *

from mongoengine import connect

uri = "mongodb+srv://zhowtenkooleksiy:OdqjdrrgrJDD64qf@db-hw2-08.u8lqztr.mongodb.net/?retryWrites=true&w=majority"

connect(
    db="hw2_09db",
    host=uri,
)


def search_quotes(query):
    if query.startswith("name:"):
        author_name = query.replace("name:", "").strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return quotes.to_json().encode("utf-8")
        else:
            return b"No quotes found for the specified author."

    elif query.startswith("tag:"):
        tag = query.replace("tag:", "").strip()
        quotes = Quote.objects(tags=tag)
        return quotes.to_json().encode("utf-8")

    elif query.startswith("tags:"):
        tags = query.replace("tags:", "").strip().split(",")
        quotes = Quote.objects(tags__in=tags)
        return quotes.to_json().encode("utf-8")

    elif query == "exit":
        return b"Exiting the script..."

    else:
        return b"Invalid query. Please try again."


# Головний цикл виконання скрипту
while True:
    user_input = input(
        "Введите команду (команда: значення, например: name: author_name, tag: tag_name, tags: tag1,tag2))"
    )
    result = search_quotes(user_input)
    print(result.decode("utf-8"))
    if user_input == "exit":
        break
