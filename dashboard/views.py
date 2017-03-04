from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import ContextMixin, TemplateView, TemplateResponseMixin


class LoginRequiredMixin(object):
    # @classmethod
    # def as_view(cls, **kwargs):
    #     view = super(LoginRequiredMixin, cls).as_view(**kwargs)
    #     return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "about.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
        context['title'] = "This is a Template View"
        return context


class MyView(LoginRequiredMixin, ContextMixin, TemplateResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "This is a Normal View with some Mixins"
        return self.render_to_response(context)


class LoginTemplateView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(LoginTemplateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Login"
        return context


class LogoutTemplateView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(LogoutTemplateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Logout"
        return context
