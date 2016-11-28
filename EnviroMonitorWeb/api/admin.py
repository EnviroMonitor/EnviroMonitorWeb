from django.contrib import admin
from django import forms
from .models import Station, Metering, Project

class StationAdminForm(forms.ModelForm):

    class Meta:
        model = Station
        fields = '__all__'


class StationAdmin(admin.ModelAdmin):
    form = StationAdminForm
    list_display = ['name', 'created', 'last_updated', 'type', 'notes', 'test', 'position', 'country', 'state', 'county', 'community', 'city', 'district']
    readonly_fields = ['created', 'last_updated']
    
admin.site.register(Station, StationAdmin)


class MeteringAdminForm(forms.ModelForm):

    class Meta:
        model = Metering
        fields = '__all__'


class MeteringAdmin(admin.ModelAdmin):
    form = MeteringAdminForm
    list_display = ['created', 'pm01', 'pm25', 'pm10', 'temp_out1', 'temp_out2', 'temp_out3', 'hum_out1', 'hum_out2', 'hum_out3', 'temp_int1', 'hum_int1', 'rssi', 'bpress_out1']
    readonly_fields = ['created']
admin.site.register(Metering, MeteringAdmin)


class ProjectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'project_website', 'description', 'logo']

admin.site.register(Project, ProjectAdmin)


