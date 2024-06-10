from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = 'Generate a new SECRET_KEY for django project distribution'

    def add_arguments(self, parser):
        parser.add_argument(
            '--prefix',
            help='Prefix for SECRET_KEY',
        )

        parser.add_argument(
            '--suffix',
            help='Suffix for SECRET_KEY',
        )

    def handle(self, *args, **options):
        secret_key = get_random_secret_key()

        if options['suffix']:
            secret_key = secret_key + options['suffix']

        if options['prefix']:
            secret_key = options['prefix'] + secret_key

        self.stdout.write(
            "SECRET_KEY={}".format(self.style.SUCCESS(secret_key))
        )
