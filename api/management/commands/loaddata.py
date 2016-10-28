import os
import csv

from django.core.management.base import BaseCommand

from api.models import Disease, Sample


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            dest='path',
            default='data',
            help='Path to location of data files.',
        )

    def handle(self, *args, **options):
        # Diseases
        disease_table_is_empty = Disease.objects.count() == 0
        if disease_table_is_empty:
            disease_path = os.path.join(options['path'], 'diseases.tsv')
            with open(disease_path) as disease_file:
                disease_reader = csv.DictReader(disease_file, delimiter='\t')
                for row in disease_reader:
                    Disease.objects.create(
                        acronym=row['acronym'],
                        name=row['disease']
                    )

        # Samples
        sample_table_is_empty = Sample.objects.count() == 0
        if sample_table_is_empty:
            # Django's ORM requires Python's None for null values... this filters accordingly
            check_null = lambda val: val if val else None
            sample_path = os.path.join(options['path'], 'samples.tsv')
            with open(sample_path) as sample_file:
                sample_reader = csv.DictReader(sample_file, delimiter='\t')
                for row in sample_reader:
                    disease = Disease.objects.get(acronym=row['acronym'])
                    Sample.objects.create(
                        sample_id=row['sample_id'],
                        disease=disease,
                        gender=check_null(row['gender']),
                        age_diagnosed=check_null(row['age_diagnosed'])
                    )
