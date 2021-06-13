from rest_framework import generics, response

from fifa import serializers, models, pagination, permissions


class TeamAPIView(generics.GenericAPIView):
    """Api that allowes search players by team name
    """
    pagination_class = pagination.CustomPagination
    permission_classes = (permissions.CustomPermission, )

    def post(self, request):
        params = serializers.TeamParamsSerializer(data=request.data)
        params.is_valid(raise_exception=True)

        team_name = params.data.get('Name')
        team = models.Team.objects.filter(name__icontains=team_name).first()
        players = models.Player.objects.filter(team=team)

        page = self.paginator.paginate_queryset(players, request)

        serializer = serializers.PlayerSerializer(page, many=True)

        return self.paginator.get_paginated_response(serializer.data)


class PlayerAPIView(generics.GenericAPIView):
    """Api that allows search players by player name
    """
    pagination_class = pagination.CustomPagination
    permission_classes = (permissions.CustomPermission, )

    def get(self, request):
        params = serializers.PlayerParamsSerializer(data=request.query_params)
        params.is_valid(raise_exception=True)

        search = params.data.get('search')

        players = models.Player.objects.filter(name__icontains=search)

        if params.data.get('sort') == 'desc':
            players = players.order_by('-name')
        
        page = self.paginator.paginate_queryset(players, request)

        serializer = serializers.PlayerSerializer(page, many=True)

        return self.paginator.get_paginated_response(serializer.data)
