from rest_framework import serializers

from fifa import models


class TeamParamsSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True)
    Page = serializers.IntegerField(required=True, min_value=1)


class PlayerParamsSerializer(serializers.Serializer):
    search = serializers.CharField(required=True)
    sort = serializers.ChoiceField(choices=['asc', 'desc'],
        default='asc', required=False)
    page = serializers.IntegerField(min_value=1, required=False)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'
