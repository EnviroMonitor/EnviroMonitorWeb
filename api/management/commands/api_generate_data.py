from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from tqdm import tqdm

from api.tests.factories import ProjectFactory, StationFactory, MeteringFactory


class Command(BaseCommand):
    DEFAULT_PROJECTS = 10
    DEFAULT_STATIONS = 10
    DEFAULT_METERINGS = 5000
    DEFAULT_METERING_DELTA = timezone.timedelta(minutes=15)

    help = 'Populate models with some data, see arguments for possible details.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--projects',
            action='store',
            default=self.__class__.DEFAULT_PROJECTS,
            help='How many Project to create? default={}.'.format(
                self.__class__.DEFAULT_PROJECTS
            ),
            type=int
        )
        parser.add_argument(
            '-s',
            '--stations',
            action='store',
            default=self.__class__.DEFAULT_STATIONS,
            help='How many Station for each Project to create? default={}.'.format(
                self.__class__.DEFAULT_STATIONS
            ),
            type=int
        )
        parser.add_argument(
            '-m',
            '--meterings',
            action='store',
            default=self.__class__.DEFAULT_METERINGS,
            help='How many Metering for each Station to create? default={}.'.format(
                self.__class__.DEFAULT_METERINGS
            ),
            type=int
        )

    @transaction.atomic()
    def handle(self, *args, **options):
        total = options['projects'] * options['stations'] * options['meterings']
        with tqdm(total=total) as progress_bar:
            for _ in range(0, options['projects']):
                project = ProjectFactory.create()
                for _ in range(0, options['stations']):
                    station = StationFactory.create(project=project)
                    for i in range(0, options['meterings']):
                        created = timezone.now() - i * self.__class__.DEFAULT_METERING_DELTA
                        MeteringFactory.create(station=station, created=created)
                        progress_bar.update(1)
