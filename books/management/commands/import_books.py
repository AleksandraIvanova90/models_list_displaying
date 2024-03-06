import json
import os
from pathlib import Path
from pprint import pprint

from django.core.management import BaseCommand

from books.models import Book

#
# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         pass
#
#     def handle(self, *args, **options):
#         p = Path.cwd()
#         path = r'fixtures\books.json'
#         with open(f'{p}\{path}', 'r', encoding='utf-8') as file:
#             books = json.load(file)
#
#         for book in books:
#             # TODO: Добавьте сохранение модели
#             Book(
#                 id=book['pk'],
#                 name=book['fields']['name'],
#                 author=book['fields']['author'],
#                 pub_date=book['fields']['pub_date'],
#
#             ).save()