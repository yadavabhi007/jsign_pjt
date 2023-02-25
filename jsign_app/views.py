from django.urls import reverse_lazy
from django.views import generic
from .models import Signature


class ExampleCreateView(generic.CreateView):
    model = Signature
    fields = '__all__'
    success_url = reverse_lazy('list')


class ExampleUpdateView(generic.UpdateView):
    model = Signature
    fields = '__all__'
    success_url = reverse_lazy('list')


class ExampleListView(generic.ListView):
    model = Signature

    