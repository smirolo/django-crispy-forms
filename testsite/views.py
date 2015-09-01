from django.views.generic import CreateView

from .forms import IndexForm


class IndexView(CreateView):

    form_class = IndexForm
    template_name = 'index.html'
