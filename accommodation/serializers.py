from renting.models import Houses
from rest_framework import serializers

class HousesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'

