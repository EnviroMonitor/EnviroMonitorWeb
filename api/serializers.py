from .models import Station, Metering, Project

from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault


class StationSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Station
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
            'owner'
        )


class MeteringSerializer(ModelSerializer):
    class Meta:
        model = Metering
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


class ProjectSerializer(ModelSerializer):
    project_admin = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Project
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
            'project_website',
            'description',
            'logo',
            'project_admin'
        )
