from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ComandoModelForm
from django.contrib import messages
from .models import ComandoModel


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class PythonView(TemplateView):
    """
    View retorna todos os registros do banco da tecnologia python
    """
    template_name = 'python.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['python'] = ComandoModel.objects.filter(tecnologia='PY')
        return context


class BashView(TemplateView):
    """
    View retorna todos os registros do banco da tecnologia bash
    """
    template_name = 'bash.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['bash'] = ComandoModel.objects.filter(tecnologia='SH')
        return context


class SqlView(TemplateView):
    """
    View retorna todos os registros do banco da tecnologia SQL
    """
    template_name = 'sql.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['sql'] = ComandoModel.objects.filter(tecnologia='SQL')
        return context


class GitView(TemplateView):
    """
    View retorna todos os registros do banco da tecnologia GIT
    """
    template_name = 'git.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['git'] = ComandoModel.objects.filter(tecnologia='GIT')
        return context


def registra_comando(request):
    # se o usuário estiver logado
    if str(request.user) != 'AnonymousUser':

        # se a requisição é do método POST
        if str(request.method) == 'POST':
            # instancia o objeto passando como parâmetro o request
            novocomando = ComandoModelForm(request.POST)

            # se o formulário é válido. Tudo digitado corretamente.
            if novocomando.is_valid():
                # salvando no banco
                novocomando.save()

                # mensagem de sucesso
                messages.success(request, 'Novo comando salvo com sucesso')

                # limpando formulário
                novocomando = ComandoModelForm()

            else:
                messages.error(request, 'Houve algum erro ao salvar o comando.')

        # se não é do tipo post, apenas instancia o objeto
        else:
            novocomando = ComandoModelForm()

        # retorno do objeto na renderização da página
        context = {
            'comando': novocomando
        }
        return render(request, 'registracomando.html', context)

    # se não tem usuário logado, redirecionado pra index
    else:
        return redirect('index')
