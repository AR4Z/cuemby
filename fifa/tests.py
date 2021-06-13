from rest_framework import test, status
from django import urls

from fifa import models, serializers

TEST_API_KEY = 'some random string'

class FifaAPITests(test.APITestCase):
    """Test general setup of fifa api
    """
    def test_call_with_invalid_api_key(self):
        TEAM_URL = urls.reverse('team')
        response = self.client.post(TEAM_URL, {
            'Name': 'real madrid',
            'Page': 1
        })

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    @test.override_settings(API_KEY=TEST_API_KEY)
    def test_call_with_valid_api_key(self):
        TEAM_URL = urls.reverse('team')
        response = self.client.post(TEAM_URL, {
            'Name': 'real madrid',
            'Page': 1
        }, **{'HTTP_X_API_KEY': TEST_API_KEY})

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITests(test.APITestCase):
    """Test setup of team api
    """
    fixtures = ['fifa/fixtures/team.json', 'fifa/fixtures/player.json']

    @test.override_settings(API_KEY=TEST_API_KEY)
    def test_team_search(self):
        TEAM_SEARCH_URL = urls.reverse('team')
        TEAM_NAME = 'real madRID'

        response = self.client.post(TEAM_SEARCH_URL, {
            'Name': TEAM_NAME,
            'Page': 1
        }, **{'HTTP_X_API_KEY': TEST_API_KEY})


        team = models.Team.objects.filter(
            name__icontains=TEAM_NAME).first()
        players = models.Player.objects.filter(team=team)


        self.assertEqual(response.data['totalItems'], players.count())

        players = players[:response.data['Items']]
        players = serializers.PlayerSerializer(players, many=True)

        self.assertEqual(response.data['Players'], players.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    


class PlayerAPITests(test.APITestCase):
    """test setup of player api
    """
    fixtures = ['fifa/fixtures/team.json', 'fifa/fixtures/player.json']

    @test.override_settings(API_KEY=TEST_API_KEY)
    def test_player_search(self):
        PLAYER_SEARCH_URL = urls.reverse('player')
        PLAYER_NAME = 'cristi'

        response = self.client.get(PLAYER_SEARCH_URL, {
            'search': PLAYER_NAME,
            'page': 1},
            **{'HTTP_X_API_KEY': TEST_API_KEY})
        
        players = models.Player.objects.filter(name__icontains=PLAYER_NAME)

        self.assertEqual(response.data['totalItems'], players.count())

        players = players[:response.data['Items']]
        players = serializers.PlayerSerializer(players, many=True)

        self.assertEqual(response.data['Players'], players.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
