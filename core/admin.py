from django.contrib import admin
from .models import ComandoModel


# Register your models here.
@admin.register(ComandoModel)
class ComandoModelAdm(admin.ModelAdmin):
    list_display = ('desenvolvedor', 'tecnologia', 'comando', 'criado')
