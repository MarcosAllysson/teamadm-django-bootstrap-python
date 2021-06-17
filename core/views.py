from django.shortcuts import render, redirect
from .forms import ComandoModelForm
from django.contrib import messages
from .models import ComandoModel


# Create your views here.
def index(request):
    return render(request, 'index.html')


def python(request):
    """
    View retorna todos os registros do banco da tecnologia python
    """
    context = {
        'python': ComandoModel.objects.filter(tecnologia='PY')
    }
    return render(request, 'python.html', context)


def bash(request):
    """
    View retorna todos os registros do banco da tecnologia bash
    """
    text = {
        'bash': ComandoModel.objects.filter(tecnologia='SH')
    }
    return render(request, 'bash.html', text)


def sql(request):
    """
    View retorna todos os registros do banco da tecnologia SQL
    """
    text = {
        'sql': ComandoModel.objects.filter(tecnologia='SQL')
    }
    return render(request, 'sql.html', text)


def git(request):
    """
    View retorna todos os registros do banco da tecnologia GIT
    """
    text = {
        'git': ComandoModel.objects.filter(tecnologia='GIT')
    }
    return render(request, 'git.html', text)


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
