from django.conf.urls import url, include
from django.views.generic import TemplateView
from mediazon.views import gender


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^api', gender, name='gender-api'),
    ]