
from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = 'Command to load fixture data'

    def handle(self, *args, **options):
        management.call_command('loaddata', 'team.json')
        management.call_command('loaddata', 'player.json')

        self.stdout.write(self.style.SUCCESS('Successfully load data'))
