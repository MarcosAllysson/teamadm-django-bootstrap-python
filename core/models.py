from django.db import models


# Create your models here.
class ComandoModel(models.Model):
    # Desenvolvedores do projeto
    DESENVOLVEDORES = [
        ('Marcos', 'Marcos Allysson'),
        ('Douglas', 'Douglas Shibata')
    ]

    # Tecnologias do projeto
    TECNOLOGIAS = [
        ('PY', 'Python'),
        ('SQL', 'SQL'),
        ('SH', 'Bash'),
        ('GIT', 'Git'),
    ]

    desenvolvedor = models.CharField('Desenvolvedor', max_length=50, choices=DESENVOLVEDORES)
    tecnologia = models.CharField('Tecnologia', max_length=50, choices=TECNOLOGIAS)
    comando = models.CharField('Comando', max_length=100)
    descricao = models.CharField('Descricao', max_length=500)
    criado = models.DateTimeField('Criado', auto_now_add=True)

    def __str__(self):
        return self.desenvolvedor
