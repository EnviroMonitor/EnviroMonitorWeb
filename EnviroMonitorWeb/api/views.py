from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Station, Metering, Project
from .forms import StationForm, MeteringForm, ProjectForm


class StationListView(ListView):
    model = Station


class StationCreateView(CreateView):
    model = Station
    form_class = StationForm


class StationDetailView(DetailView):
    model = Station


class StationUpdateView(UpdateView):
    model = Station
    form_class = StationForm


class MeteringListView(ListView):
    model = Metering


class MeteringCreateView(CreateView):
    model = Metering
    form_class = MeteringForm


class MeteringDetailView(DetailView):
    model = Metering


class MeteringUpdateView(UpdateView):
    model = Metering
    form_class = MeteringForm


class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
