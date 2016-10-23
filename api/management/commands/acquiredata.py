import os
from urllib.request import urlretrieve
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join('data', 'diseases.tsv')
        url = 'https://raw.githubusercontent.com/cognoma/cancer-data/master/download/diseases.tsv'
        urlretrieve(url, path)
