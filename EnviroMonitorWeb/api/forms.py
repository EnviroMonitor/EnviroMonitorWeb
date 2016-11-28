from django import forms
from .models import Station, Metering, Project


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'type', 'notes', 'test', 'position', 'country', 'state', 'county', 'community', 'city', 'district', 'owner']


class MeteringForm(forms.ModelForm):
    class Meta:
        model = Metering
        fields = ['pm01', 'pm25', 'pm10', 'temp_out1', 'temp_out2', 'temp_out3', 'hum_out1', 'hum_out2', 'hum_out3', 'temp_int1', 'hum_int1', 'rssi', 'bpress_out1', 'station']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'project_website', 'description', 'logo', 'project_admin']


