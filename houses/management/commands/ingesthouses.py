from django.core.management.base import BaseCommand, CommandError
from houses.models import House

class Command(BaseCommand):
    help = 'Ingests house data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
        file_name = options['file_name']

        self.stdout.write(self.style.SUCCESS('Successfully ingested Houses from: %s' % file_name))