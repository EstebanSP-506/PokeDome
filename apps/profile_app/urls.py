from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.get_trainer),
    url(r'^(?P<trainer_ID>\d+)$', views.profile),
    url(r'^(?P<trainer_ID>\d+)/remove$', views.remove),
    url(r'^(?P<trainer_ID>\d+)/edit$', views.edit),
    url(r'^(?P<trainer_ID>\d+)/add_team$', views.add_team),
    url(r'^(?P<trainer_ID>\d+)/(?P<team_ID>\d+)/select$', views.select_team),
    # url(r'^(?P<trainer_ID>\d+)/(?P<team_ID>\d+)/delete$', views.delete_team),
]
