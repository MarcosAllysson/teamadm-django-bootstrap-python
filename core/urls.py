from django.urls import path
from .views import registra_comando, IndexView, PythonView, BashView, GitView, SqlView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('python/', PythonView.as_view(), name='python'),
    path('bash/', BashView.as_view(), name='bash'),
    path('git/', GitView.as_view(), name='git'),
    path('sql/', SqlView.as_view(), name='sql'),
    path('registracomando/', registra_comando, name='registracomando'),
]
