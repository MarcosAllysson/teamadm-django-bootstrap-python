from django.urls import path
from .views import index, python, registra_comando, bash, git, sql


urlpatterns = [
    path('', index, name='index'),
    path('python/', python, name='python'),
    path('bash/', bash, name='bash'),
    path('git/', git, name='git'),
    path('sql/', sql, name='sql'),
    path('registracomando/', registra_comando, name='registracomando'),
]
