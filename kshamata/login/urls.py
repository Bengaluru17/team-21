from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^make/$', views.survey, name='survey'),
    url(r'^addt/$', views.make, name='addtrain'),
]