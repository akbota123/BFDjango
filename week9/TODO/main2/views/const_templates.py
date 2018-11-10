from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'
    http_method_names = ['get']


class DetailView(TemplateView):
    template_name = 'detail.html'
    http_method_names = ['get']