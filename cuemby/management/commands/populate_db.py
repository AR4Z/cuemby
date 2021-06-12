import requests
from django.core.management import base
from django.db import transaction

from fifa import models


class Command(base.BaseCommand):
    help = 'Command to create random data'
    FIFA_API_BASE_URL = 'https://www.easports.com/fifa/ultimate-team/api/fut/item'

    def handle(self, *args, **options):
        current_page = 1
        # some random big number greater then current_page value
        total_pages = 1000

        with transaction.atomic():
            while current_page <= total_pages:
                params = {
                    'page': current_page 
                }
                response = requests.get(self.FIFA_API_BASE_URL, params=params)
                body = response.json()
                items = body.get('items', [])

                for item in items:
                    club_info = item.get('club')
                    club_name = club_info.get('name')

                    team = self.create_team(club_name)
                    name = item.get('commonName')

                    if name == '':
                        first_name = item.get('firstName')
                        last_name = item.get('lastName')

                        name = f'{first_name} {last_name}'
                    
                    nation_info = item.get('nation')
                    nation_name = nation_info.get('name')

                    position_name = item.get('positionFull')

                    self.create_player(name, position_name, nation_name, team)

                current_page += 1
                total_pages = body.get('totalPages')
    

    def create_team(self, name: str):
        """creates team entity in Team model

        Args:
            name (str): Team's name
        """
        obj, _ = models.Team.objects.get_or_create(
            name=name
        )

        return obj
    

    def create_player(self, name: str, position: str, nation: str, team: models.Team):
        obj, _ = models.Player.objects.get_or_create(
            name=name,
            position=position,
            nation=nation,
            team=team
        )

        return obj
