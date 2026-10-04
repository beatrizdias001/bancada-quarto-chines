from django.db import models

# Create your models here.



class Funcionamento(models.Model):
    #  R01
    nome = models.CharField(max_length=20, unique=True)
    #Horário do campus
    assunto = models.CharField(max_length=100)
    # A partir de qual horário o campus começa seu funcionamento?
    pergunta = models.CharField(max_length=200)
    # Informe o horário
    trecho = models.CharField(max_length=50)
    # Funcionamento, horario
    palavras_chave = models.CharField(max_length=200)
    # Às 07h00 da manhã
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Biblioteca(models.Model):
    #  R02
    nome = models.CharField(max_length=20, unique=True)
    #Horário da biblioteca
    assunto = models.CharField(max_length=100)
    # A partir de qual horário a biblioteca abre pela manhã?
    pergunta = models.CharField(max_length=200)
    # Informe o horário de entrada na biblioteca
    trecho = models.CharField(max_length=50)
    # biblioteca horario
    palavras_chave = models.CharField(max_length=200)
    # Às 08h30 da manhã
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Emprestimo(models.Model):
    #  R03
    nome = models.CharField(max_length=20, unique=True)
    #Emprestimo de livro
    assunto = models.CharField(max_length=100)
    # Como funciona para o aluno conseguir um livro, da biblioteca do campus, emprestado?
    pergunta = models.CharField(max_length=200)
    # Informe os dados necessários para o aluno conseguir pegar um livro
    trecho = models.CharField(max_length=50)
    # biblioteca, livro, emprestimo
    palavras_chave = models.CharField(max_length=200)
    # Deve-se ir até o bibliotecário com o livro e digitar sua matrícula e senha para obter o empréstimo do livro

    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

from django.db import models


class Matricula(models.Model):
    # R04
    nome = models.CharField(max_length=10, unique=True)
    # Matrícula do aluno
    assunto = models.CharField(max_length=100)
    # O que significa os dois últimos números da matrícula dos alunos?
    pergunta = models.CharField(max_length=200)
    # Funcionalidade dos putimos dois algoritmos da matrícula
    trecho = models.CharField(max_length=50)
    # matrícula, aluno, números, significado
    palavras_chave = models.CharField(max_length=200)
    # Significa a ordem de cadastro no SUAP
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Merenda(models.Model):
    # R05
    nome = models.CharField(max_length=10, unique=True)
    # Horário merenda
    assunto = models.CharField(max_length=100)
    # Qual o horário que o refeitório abre para a merenda?
    pergunta = models.CharField(max_length=200)
    # Informe o horário que o refeitório abre
    trecho = models.CharField(max_length=50)
    # refeitório, merenda, horário
    palavras_chave = models.CharField(max_length=200)
    # O refeitório abre às 08h30 para a merenda
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Wifi(models.Model):
    # R06
    nome = models.CharField(max_length=10, unique=True)
    # Dados do wifi de visitantes
    assunto = models.CharField(max_length=100)
    # Para entrar no WI-FI dos visitantes, o que é necessário?
    pergunta = models.CharField(max_length=200)
    # Informe os dados necessários para um visitante conseguir acessar o wi-fi
    trecho = models.CharField(max_length=50)
    # wifi, dados, visitantes
    palavras_chave = models.CharField(max_length=200)
    # Precisa colocar a senha do gov.br
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Onibus(models.Model):
    # R07
    nome = models.CharField(max_length=10, unique=True)
    # horário do ônibus de tarde
    assunto = models.CharField(max_length=100)
    # Até que horário os ônibus esperam os alunos no final da tarde?
    pergunta = models.CharField(max_length=200)
    # Informe até qual horário o ônibus espera os alunos da tarde
    trecho = models.CharField(max_length=50)
    # ônibus, alunos, tarde
    palavras_chave = models.CharField(max_length=200)
    # Até às 18h00
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Servidores(models.Model):
    # R08
    nome = models.CharField(max_length=10, unique=True)
    # Saída dos servidores
    assunto = models.CharField(max_length=100)
    # Qual o horário que a maioria dos servidores acabam o seu turno de trabalho?
    pergunta = models.CharField(max_length=200)
    # Informe até qual horário, em média, os servidores saem do campus e vão para suas casas
    trecho = models.CharField(max_length=50)
    # servidores, trabalho, horario
    palavras_chave = models.CharField(max_length=200)
    # Às 16h
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Calendario(models.Model):
    # R09
    nome = models.CharField(max_length=10, unique=True)
    # Calendário Acadêmico
    assunto = models.CharField(max_length=100)
    # Onde se pode encontrar o calendário acadêmico?
    pergunta = models.CharField(max_length=200)
    # Informe em qual site se pode encontrar o calendário acadêmico
    trecho = models.CharField(max_length=50)
    # calendário, acadêmico, local
    palavras_chave = models.CharField(max_length=200)
    # O calendário encontra-se no SUAP

    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Estagiário(models.Model):
    # R10
    nome = models.CharField(max_length=10, unique=True)
    # Declaração de falta 
    assunto = models.CharField(max_length=100)
    # Com quem o estagiário precisa falar para conseguir uma declaração de falta ao trabalho?
    pergunta = models.CharField(max_length=200)
    # Informe com quem o estagiário fala para conseguir uma declarção de falta para entregar no trabalho
    trecho = models.CharField(max_length=50)
    # estagiário, declaração, trabalho
    palavras_chave = models.CharField(max_length=200)
    # O estagiário precisa falar com o coordenador do curso


    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Carteira_estudante(models.Model):
    # R11
    nome = models.CharField(max_length=10, unique=True)
    # Carteira de estudante
    assunto = models.CharField(max_length=100)
    # Todos os estudantes possuem, de forma obrigatória, carteiras de estudante?
    pergunta = models.CharField(max_length=200)
    # Informe se os estudantes precisam necessáriamente ter carteira de estudante
    trecho = models.CharField(max_length=50)
    # carteira, estudante
    palavras_chave = models.CharField(max_length=200)
    # Não. O campus não cobra a carteira estudantil


    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Auxilios(models.Model):
    # R12
    nome = models.CharField(max_length=10, unique=True)
    # Auxilio estudantil
    assunto = models.CharField(max_length=100)
    # Quais são os auxílios estudantis que o campus oferece?
    pergunta = models.CharField(max_length=200)
    # Informe quais os auxílios disponíveis pelo campus
    trecho = models.CharField(max_length=50)
    # auxpilio, estudantil
    palavras_chave = models.CharField(max_length=200)
    # O campus oferece auxílios como: moradia, alimentação, transporte e programa de apoio à formação estudantil(PAFE)
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"
