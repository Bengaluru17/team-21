from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^make/$', views.survey, name='survey'),
    url(r'^addt/$', views.make, name='addtrain'),
    url(r'^show/$', views.show, name='show'),
    url(r'^search/$',views.search, name='search'),
    url(r'^location/$', views.location, name='location')

]