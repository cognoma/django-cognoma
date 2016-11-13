import os
from urllib.request import urlretrieve

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            dest='path',
            default='data',
            help='Path to location of data files.',
        )

    def handle(self, *args, **options):
        if not os.path.exists(options['path']):
            os.makedirs(options['path'])

        disease_path = os.path.join(options['path'], 'diseases.tsv')
        if not os.path.exists(disease_path):
            disease_url = 'https://raw.githubusercontent.com/cognoma/cancer-data/master/download/diseases.tsv'
            urlretrieve(disease_url, disease_path)

        sample_path = os.path.join(options['path'], 'samples.tsv')
        if not os.path.exists(sample_path):
            sample_url = 'https://raw.githubusercontent.com/cognoma/cancer-data/master/data/samples.tsv'
            urlretrieve(sample_url, sample_path)

        gene_path = os.path.join(options['path'], 'genes.tsv')
        if not os.path.exists(gene_path):
            gene_url = 'http://www.stephenshank.com/genes.tsv'
            urlretrieve(gene_url, gene_path)

        mutation_path = os.path.join(options['path'], 'mutation-matrix.tsv.bz2')
        if not os.path.exists(mutation_path):
            mutation_url = 'https://ndownloader.figshare.com/files/5864862'
            urlretrieve(mutation_url, mutation_path)
