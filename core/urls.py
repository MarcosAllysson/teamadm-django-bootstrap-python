from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('add-comando/', views.ComandoAdd.as_view(), name='add-comando'),
    path('python/', views.PythonView.as_view(), name='python'),
    path('bash/', views.BashView.as_view(), name='bash'),
    path('git/', views.GitView.as_view(), name='git'),
    path('sql/', views.SqlView.as_view(), name='sql'),
    path('docker/', views.DockerView.as_view(), name='docker'),
    path('script/', views.ScriptView.as_view(), name='script'),
    path('rasa/', views.RasaView.as_view(), name='rasa'),
    path('django/', views.DjangoView.as_view(), name='django'),

]
