from django.views.generic import ListView, DetailView

from django.shortcuts import render

from .models import Fotbalista, Klub


class FotbalisteListView(ListView):
    model = Fotbalista
    context_object_name = "fotbaliste"
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_fotbaliste'] = len(self.get_queryset())
        return context


def index(request):
    num_fotbaliste = Fotbalista.objects.all().count()
    fotbaliste = Fotbalista.objects.order_by('-rate')[:3]

    context = {
        'num_fotbaliste': num_fotbaliste,
        'fotbaliste': fotbaliste,
    }

    return render(request, 'index.html', context=context)


class KlubyListView(ListView):
    model = Klub
    context_object_name = "kluby_list"
    template_name = "kluby.html"


class FotbalistaDetailView(DetailView):
    model = Fotbalista
    context_object_name = 'fotbalista_detail'
    template_name = 'detail.html'
