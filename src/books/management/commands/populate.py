from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = "Populates database with data from https://openlibrary.org/"

    # def add_arguments(self, parser):
    #     parser.add_argument("fname", nargs=1, type=str)
    #     parser.add_argument("value", nargs=1, type=str)

    def handle(self, *args, **options):
        fname = options.get("fname", "title")
        value = options.get("value", "nie")
        endpoint = f"https://openlibrary.org/search.json?q={fname}:{value}&fields=title,author_name,first_publish_year,ratings_average,editions"
        resp = requests.get(endpoint)
        for book in resp.json().get("docs", []):
            title = book.get("title", "")
            first_published_year = book.get("first_publish_year", None)
            rating = book.get("ratings_average", None)
            editions = book.get("editions", [])
            authors = book.get("author_name", [])
