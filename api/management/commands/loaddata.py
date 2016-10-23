import os
import csv
from django.core.management.base import BaseCommand
from api.models import Disease


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join('data', 'diseases.tsv')
        with open(path, 'r') as diseases_file:
            diseases_rows = csv.reader(diseases_file, delimiter='\t')
            # Skip header
            next(diseases_rows)
            for row in diseases_rows:
                acronym = row[0]
                name = row[1]
                Disease.objects.create(acronym=acronym, name=name)
