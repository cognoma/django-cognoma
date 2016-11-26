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
                disease_list = []
                for row in disease_reader:
                    disease = Disease(
                        acronym=row['acronym'],
                        name=row['disease']
                    )
                    disease_list.append(disease)
                Disease.objects.bulk_create(disease_list)

        # Samples
        if Sample.objects.count() == 0:
            sample_path = os.path.join(options['path'], 'samples.tsv')
            with open(sample_path) as sample_file:
                sample_reader = csv.DictReader(sample_file, delimiter='\t')
                sample_list = []
                for row in sample_reader:
                    disease = Disease.objects.get(acronym=row['acronym'])
                    sample = Sample(
                        sample_id=row['sample_id'],
                        disease=disease,
                        gender=row['gender'] or None,
                        age_diagnosed=row['age_diagnosed'] or None
                    )
                    sample_list.append(sample)
                Sample.objects.bulk_create(sample_list)

        # Genes
        if Gene.objects.count() == 0:
            gene_path = os.path.join(options['path'], 'genes.tsv')
            with open(gene_path) as gene_file:
                gene_reader = csv.DictReader(gene_file, delimiter='\t')
                gene_list = []
                for row in gene_reader:
                    gene = Gene(
                        entrez_gene_id=row['entrez_gene_id'],
                        symbol=row['symbol'],
                        description=row['description'],
                        chromosome=row['chromosome'] or None,
                        gene_type=row['gene_type'],
                        synonyms=row['synonyms'].split('|') or None,
                        aliases=row['aliases'].split('|') or None
                    )
                    gene_list.append(gene)
                Gene.objects.bulk_create(gene_list)
