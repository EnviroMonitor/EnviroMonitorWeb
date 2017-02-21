import uuid
from django.conf import settings
from django.core.cache import cache
from django.contrib.gis.db import models as gis_models
from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.fields import AutoSlugField

from .utils import generate_token


class AbstractTimeTrackable(models.Model):
    """
    Abstract model for time trackable features.
    """

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class AbstractMetering(models.Model):
    """
    Abstract model for Metering and MeteringHistory models.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    # Data Fields
    pm01 = models.FloatField(
        help_text='PM 0.1 in ug/m^3'
    )
    pm25 = models.FloatField(
        help_text='PM 2.5 in ug/m^3'
    )
    pm10 = models.FloatField(
        help_text='PM 10 in ug/m^3'
    )
    temp_out1 = models.FloatField(
        help_text='Outside temperature sensor1, in C.'
    )
    temp_out2 = models.FloatField(
        help_text='Outside temperature sensor2, optional, in C.',
        blank=True,
        default=None,
        null=True
    )
    temp_out3 = models.FloatField(
        help_text='Outside temperature sensor3, optional, in C.',
        blank=True,
        default=None,
        null=True
    )
    temp_int_air1 = models.FloatField(
        help_text='Internal temperature sensor1 (air sucked by PM sensor), in C.'
    )
    hum_out1 = models.FloatField(
        help_text='Outside relative humidity sensor1, in %.'
    )
    hum_out2 = models.FloatField(
        help_text='Outside relative humidity sensor2, optional, in %.',
        blank=True,
        default=None,
        null=True
    )
    hum_out3 = models.FloatField(
        help_text='Outside relative humidity sensor3, optional, in %.',
        blank=True,
        default=None,
        null=True
    )
    hum_int_air1 = models.FloatField(
        help_text='Internal relative humidity sensor1 (air sucked by PM sensor), in %.'
    )
    rssi = models.FloatField(
        help_text='RSSI of WiFi (signal strength). For debugging "vanishing" stations.'
    )
    bpress_out1 = models.FloatField(
        help_text='Outside absolute barometric pressure sensor1, in hPa.'
    )

    # Relationship Fields
    station = models.ForeignKey('api.Station')

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.created


class AbstractLocation(models.Model):
    """
    Abstract model for location features.
    """

    position = gis_models.PointField(help_text='Exact position on map.', default=None, null=True)
    country = models.CharField(max_length=255, default='')
    state = models.CharField(help_text='administration level 1', max_length=255, default='')
    county = models.CharField(help_text='administration level 2', max_length=255, default='')
    community = models.CharField(help_text='administration level 3', max_length=255, default='')
    city = models.CharField(help_text='administration level 4', max_length=255, default='')
    district = models.CharField(help_text='administration level 5', max_length=255, default='')

    class Meta:
        abstract = True


class Station(AbstractTimeTrackable, AbstractLocation):
    """
    Model representing sensor station. Can be grouped using Project model.
    """

    EM0 = '1'
    EM1 = '2'
    CUSTOM = '3'
    TYPE_CHOICES = (
        (EM0, 'EM0.1'),
        (EM1, 'EM1'),
        (CUSTOM, 'CUSTOM'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    notes = models.CharField(max_length=255)
    is_in_test_mode = models.BooleanField(
        help_text='Whether sensor is in test mode or not (all data).',
        default=False
    )
    token = models.CharField(
        max_length=255,
        help_text='Token automatically generated while saving model, needed by Station to POST any data.',
        default=generate_token,
        unique=True
    )
    altitude = models.FloatField(help_text='Altitude of sensor location.', default=0)

    # Relationship Fields
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey('api.Project')

    @property
    def last_metering(self):
        """
        Return lastly created, serialized Metering object.
        We remove cache key while adding metering to given station.
        """
        if not cache.get(self.last_metering_cache_key):
            from api.serializers import MeteringSerializer
            last_metering = self.metering_set.first()
            cache.set(self.last_metering_cache_key, MeteringSerializer(last_metering).data)
        return cache.get(self.last_metering_cache_key)

    @property
    def last_metering_cache_key(self):
        return u'station-{}-last-metering'.format(self.pk)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('api_station_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('api_station_update', args=(self.id,))


class Metering(AbstractMetering):
    """
    Model representing data submitted by sensor station.
    """

    is_test = models.BooleanField(
        help_text='Whether entry was created using Sensor test mode (Sensor.is_in_test_mode=True).',
        default=False,
        db_index=True
    )

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('api_metering_detail', args=(self.pk,))


class MeteringHistory(AbstractMetering):
    """
    Model representing history entries calculated from Metering entries, resolution 1 hour.

    Idea:
    * background job runs once per hour
    * job calculates avarage of readings from Metering entries older than 2 weeks (avarage
    should be calulated per hour basis, one MeteringHistory entry per hour)
    * entries that was used to calculate avarage should be cleaned from Metering database
    """

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('api_meteringhistory_detail', args=(self.pk,))


class Project(AbstractTimeTrackable, AbstractLocation):
    """
    Model used for grouping sensor stations. Eg. by local anti-smog groups.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True, unique=True)

    website = models.URLField()
    description = models.TextField()
    logo = models.ImageField(max_length=100, upload_to='project/', blank=True, null=True, default=None)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('api_project_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('api_project_update', args=(self.slug,))
