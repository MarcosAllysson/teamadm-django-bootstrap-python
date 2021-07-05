from django.db import models


# Modelo
class ComandoModel(models.Model):
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
        ('DJANGO', 'Django'),
        ('RASA', 'Rasa'),
        ('SCRIPT', 'Script'),
        ('DOCKER', 'Docker'),
    ]

    desenvolvedor = models.CharField('Desenvolvedor', max_length=50, choices=DESENVOLVEDORES)
    tecnologia = models.CharField('Tecnologia', max_length=50, choices=TECNOLOGIAS)
    comando = models.CharField('Comando', max_length=255)
    descricao = models.TextField('Descrição')
    criado = models.DateTimeField('Criado', auto_now_add=True)

    def __str__(self):
        return self.desenvolvedor

    class Meta:
        ordering = ['-criado']
