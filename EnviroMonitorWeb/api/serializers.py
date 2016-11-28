import models

from rest_framework import serializers


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Station
        fields = (
            'id', 
            'name', 
            'created', 
            'last_updated', 
            'type', 
            'notes', 
            'test', 
            'position', 
            'country', 
            'state', 
            'county', 
            'community', 
            'city', 
            'district', 
        )


class MeteringSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Metering
        fields = (
            'id', 
            'created', 
            'pm01', 
            'pm25', 
            'pm10', 
            'temp_out1', 
            'temp_out2', 
            'temp_out3', 
            'hum_out1', 
            'hum_out2', 
            'hum_out3', 
            'temp_int1', 
            'hum_int1', 
            'rssi', 
            'bpress_out1', 
        )


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'project_website', 
            'description', 
            'logo', 
        )


