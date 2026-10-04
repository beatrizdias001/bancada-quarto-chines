from django.contrib import admin

# Register your models here.


from .models import Funcionamento


@admin.register(Funcionamento)
class FuncionamentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Biblioteca


@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Emprestimo


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Matricula


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Merenda


@admin.register(Merenda)
class MerendaAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Wifi


@admin.register(Wifi)
class WifiAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Onibus


@admin.register(Onibus)
class OnibusAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Servidores


@admin.register(Servidores)
class ServidoresAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Calendario


@admin.register(Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Estagiário


@admin.register(Estagiário)
class EstagiarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Carteira_estudante


@admin.register(Carteira_estudante)
class Carteira_estudante(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]

from .models import Auxilios


@admin.register(Auxilios)
class AuxiliosAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]


