from factory.django import DjangoModelFactory

from api.models import Station, Metering, Project


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project


class StationFactory(DjangoModelFactory):
    class Meta:
        model = Station


class MeteringFactory(DjangoModelFactory):
    class Meta:
        model = Metering
