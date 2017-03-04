from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView

# Create your views here.


@login_required
class DashboardTemplateView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
        context['title'] = "This is a Test PLOP!!"
        return context


class MyView(View):
    pass
