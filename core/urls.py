from django.urls import path
from .views import index, python, registra_comando, bash


urlpatterns = [
    path('', index, name='index'),
    path('python/', python, name='python'),
    path('bash/', bash, name='bash'),
    path('registracomando/', registra_comando, name='registracomando'),
]
