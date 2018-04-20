from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.pokedex),
    url(r'^builder$', views.pokedex_builder),
    url(r'^(?P<poke_ID>\d+)$', views.get_pokemon),
    url(r'^(?P<poke_ID>\d+)/add$', views.add2team),
]
