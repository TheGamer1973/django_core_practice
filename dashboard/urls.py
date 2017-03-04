from django.conf.urls import url
from .views import DashboardTemplateView, MyView

urlpatterns = [
    url(r'^$', DashboardTemplateView.as_view(), name='main'),
    url(r'^someview/$', MyView.as_view(), name='someview'),
]
