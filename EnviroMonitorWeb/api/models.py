from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Station(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.TextField(max_length=100)
    notes = models.TextField(max_length=100)
    test = models.BooleanField()
    position = models.TextField(max_length=100)
    country = models.TextField(max_length=30)
    state = models.TextField(max_length=100)
    county = models.TextField(max_length=100)
    community = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    district = models.TextField(max_length=100)

    # Relationship Fields
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, )
    project = models.ForeignKey('api.Project', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('api_station_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('api_station_update', args=(self.id,))


class Metering(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True)
    pm01 = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    temp_out1 = models.FloatField()
    temp_out2 = models.FloatField(max_length=100)
    temp_out3 = models.FloatField()
    hum_out1 = models.FloatField()
    hum_out2 = models.FloatField()
    hum_out3 = models.FloatField()
    temp_int1 = models.FloatField()
    hum_int1 = models.TextField(max_length=100)
    rssi = models.FloatField()
    bpress_out1 = models.FloatField()

    # Relationship Fields
    station = models.ForeignKey('api.Station', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('api_metering_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('api_metering_update', args=(self.id,))


class Project(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    project_website = models.URLField()
    description = models.TextField(max_length=4000)
    logo = models.FilePathField(max_length=100, blank=True)

    # Relationship Fields
    project_admin = models.ForeignKey(settings.AUTH_USER_MODEL, )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('api_project_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('api_project_update', args=(self.slug,))


