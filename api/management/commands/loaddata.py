import os
import csv

from django.core.management.base import BaseCommand
import pandas as pd

from api.models import Disease, Sample, Gene, Mutation


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
        if Disease.objects.count() == 0:
            disease_path = os.path.join(options['path'], 'diseases.tsv')
            with open(disease_path) as disease_file:
                disease_reader = csv.DictReader(disease_file, delimiter='\t')
                for row in disease_reader:
                    Disease.objects.create(
                        acronym=row['acronym'],
                        name=row['disease']
                    )

        # Samples
        if Sample.objects.count() == 0:
            sample_path = os.path.join(options['path'], 'samples.tsv')
            with open(sample_path) as sample_file:
                sample_reader = csv.DictReader(sample_file, delimiter='\t')
                for row in sample_reader:
                    disease = Disease.objects.get(acronym=row['acronym'])
                    Sample.objects.create(
                        sample_id=row['sample_id'],
                        disease=disease,
                        gender=row['gender'] or None,
                        age_diagnosed=row['age_diagnosed'] or None
                    )

        # Genes
        if Gene.objects.count() == 0:
            gene_path = os.path.join(options['path'], 'genes.tsv')
            with open(gene_path) as gene_file:
                gene_reader = csv.DictReader(gene_file, delimiter='\t')
                for row in gene_reader:
                    Gene.objects.create(
                        entrez_gene_id=row['entrez_gene_id'],
                        symbol=row['symbol'],
                        description=row['description'],
                        chromosome=row['chromosome'] or None,
                        gene_type=row['gene_type'],
                        synonyms=row['synonyms'] or None,
                        aliases=row['aliases'] or None
                    )

