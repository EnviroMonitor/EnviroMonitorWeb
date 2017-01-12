from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from .models import Station, Metering, Project, MeteringHistory


class StationSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Station
        fields = (
            'id',
            'name',
            'created',
            'updated',
            'type',
            'notes',
            'is_in_test_mode',
            'altitude',
            'position',
            'country',
            'state',
            'county',
            'community',
            'city',
            'district',
            'owner',
            'project'
        )


class MeteringSerializer(ModelSerializer):
    class Meta:
        model = Metering
        fields = (
            'created',
            'pm01',
            'pm25',
            'pm10',
            'temp_out1',
            'temp_out2',
            'temp_out3',
            'temp_int1',
            'hum_out1',
            'hum_out2',
            'hum_out3',
            'hum_int1',
            'rssi',
            'bpress_out1',
        )


class MeteringHistorySerializer(ModelSerializer):
    class Meta(MeteringSerializer.Meta):
        model = MeteringHistory


class ProjectSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Project
        fields = (
            'name',
            'slug',
            'created',
            'updated',
            'website',
            'description',
            'logo',
            'owner'
        )
