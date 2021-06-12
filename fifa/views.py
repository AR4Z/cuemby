from rest_framework import views, response

from fifa import serializers
from fifa import models


class TeamAPIView(views.APIView):
    def post(self, request):
        params = serializers.TeamParamsSerializer(data=request.data)
        params.is_valid(raise_exception=True)

        team_name = params.data.get('Name')
        team = models.Team.objects.filter(name__icontains=team_name).first()
        players = models.Player.objects.filter(team=team)

        serializer = serializers.PlayerSerializer(players, many=True)

        return response.Response(serializer.data)


class PlayerAPIView(views.APIView):
    def get(self, request):
        params = serializers.PlayerParamsSerializer(data=request.query_params)
        params.is_valid(raise_exception=True)

        search = params.data.get('search')

        players = models.Player.objects.filter(name__icontains=search)

        if params.data.get('sort') == 'desc':
            players = players.order_by('-name')

        serializer = serializers.PlayerSerializer(players, many=True)

        return response.Response(serializer.data)
