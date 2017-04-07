from rest_framework import  serializers

from .models import Station, Metering, Project, MeteringHistory


class StationSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
            'project',
            'last_metering',
        )


class MeteringSerializer(serializers.ModelSerializer):
    pm01 = serializers.FloatField(default=None, write_only=True)
    temp_out2 = serializers.FloatField(default=None, write_only=True)
    temp_out3 = serializers.FloatField(default=None, write_only=True)
    temp_int_air1 = serializers.FloatField(default=None, write_only=True)
    hum_out2 = serializers.FloatField(default=None, write_only=True)
    hum_out3 = serializers.FloatField(default=None, write_only=True)
    hum_int_air1 = serializers.FloatField(default=None, write_only=True)
    rssi = serializers.FloatField(default=None, write_only=True)
    bpress_out1 = serializers.FloatField(default=None, write_only=True)

    class Meta:
        model = Metering
        fields = (
            'station',
            'created',
            'pm01',
            'pm25',
            'pm10',
            'temp_out1',
            'temp_out2',
            'temp_out3',
            'temp_int_air1',
            'hum_out1',
            'hum_out2',
            'hum_out3',
            'hum_int_air1',
            'rssi',
            'bpress_out1',
            'hw_id',
        )


class MeteringHistorySerializer(serializers.ModelSerializer):
    class Meta(MeteringSerializer.Meta):
        model = MeteringHistory


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
            'position',
            'country',
            'state',
            'county',
            'community',
            'city',
            'district',
            'owner',
        )
