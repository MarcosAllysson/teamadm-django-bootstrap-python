from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ComandoModel


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_field_name = True

    def get_success_url(self):
        return reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class IndexView(TemplateView):
    model = ComandoModel
    template_name = 'index.html'


class ComandoAdd(LoginRequiredMixin, CreateView):
    model = ComandoModel
    fields = ['desenvolvedor', 'tecnologia', 'comando', 'descricao']
    template_name = 'comando_form.html'
    success_url = reverse_lazy('index')


class PythonView(ListView):
    """
    View retorna todos os registros do banco da tecnologia python
    """
    model = ComandoModel
    template_name = 'python.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['python'] = ComandoModel.objects.filter(tecnologia='PY')
        return context


class BashView(ListView):
    """
    View retorna todos os registros do banco da tecnologia bash
    """
    model = ComandoModel
    template_name = 'bash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bash'] = ComandoModel.objects.filter(tecnologia='SH')
        return context


class SqlView(ListView):
    """
    View retorna todos os registros do banco da tecnologia SQL
    """
    model = ComandoModel
    template_name = 'sql.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sql'] = ComandoModel.objects.filter(tecnologia='SQL')
        return context


class GitView(ListView):
    """
    View retorna todos os registros do banco da tecnologia GIT
    """
    model = ComandoModel
    template_name = 'git.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['git'] = ComandoModel.objects.filter(tecnologia='GIT')
        return context


class DockerView(ListView):
    model = ComandoModel
    template_name = 'docker.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docker'] = ComandoModel.objects.filter(tecnologia='DOCKER')
        return context


class ScriptView(ListView):
    model = ComandoModel
    template_name = 'script.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['script'] = ComandoModel.objects.filter(tecnologia='SCRIPT')
        return context


class RasaView(ListView):
    model = ComandoModel
    template_name = 'rasa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rasa'] = ComandoModel.objects.filter(tecnologia='RASA')
        return context


class DjangoView(ListView):
    model = ComandoModel
    template_name = 'django.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['django'] = ComandoModel.objects.filter(tecnologia='DJANGO')
        return context
