from django.views.generic import CreateView, DeleteView,DetailView, ListView, TemplateView, UpdateView
from .models import Snack
from django.urls import reverse_lazy

class AboutPageView(TemplateView):
  template_name = 'about.html'

class SnackListView(ListView):
  template_name = 'snacks_list.html'
  model = Snack

class SnackDetailView(DetailView):
  template_name = 'snacks_detail.html'
  model = Snack

class SnackCreateView(CreateView):
  template_name = 'snacks_create.html'
  model = Snack
  fields = ['name', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
  template_name = 'snacks_update.html'
  model = Snack
  fields = "__all__"

class SnackDeleteView(DeleteView):
  template_name = 'snacks_delete.html'
  model = Snack
  success_url = reverse_lazy("snacks_list")
