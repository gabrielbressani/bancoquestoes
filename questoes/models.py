from django.db import models
from django.urls import reverse

from model_utils.managers import InheritanceManager


class Questao(models.Model):
    """
    Classe base para Questões.

    texto_questao (str) = Texto da questão, seu enunciado ou pergunta.
    """
    texto_questao = models.CharField(max_length=1000,
                                     blank=False, null=False,
                                     help_text="Insira o texto da questão.",
                                     verbose_name="Texto da Questão")
    objects = InheritanceManager()

    def __str__(self):
        return self.texto_questao


class QuestaoObjetiva(Questao):
    """
    Questão do tipo objetiva, herda de Questão e possui uma lista de Respostas
    """

    def get_absolute_url(self):
        return reverse('update-objetiva', kwargs={'pk': self.pk})

    @property
    def cname(self):
        return 'objetiva'

    class Meta:
        verbose_name = "Questão Objetiva"
        verbose_name_plural = "Questões Objetivas"


class QuestaoDiscursiva(Questao):
    """
    Questão do tipo discursiva, herda de Questão e possui uma única Respostas Discursiva
    """

    def get_absolute_url(self):
        return reverse('update-discursiva', kwargs={'pk': self.pk})

    @property
    def cname(self):
        return 'discursiva'

    class Meta:
        verbose_name = "Questão Discursiva"
        verbose_name_plural = "Questões Discursivas"


class Resposta(models.Model):
    """
    Repostas possíveis para uma Questão objetiva

    questao (fk) - Id da QuestãoObjetiva a qual essa resposta pertence.
    texto_resposta - O texto da resposta.
    correct - Se é ou não a ou uma das respostas corretas.
    """
    questao = models.ForeignKey(QuestaoObjetiva, verbose_name="Questao")

    texto_resposta = models.CharField(max_length=1000,
                                      blank=False, null=False,
                                      help_text="Insira o texto da resposta.",
                                      verbose_name="Texto da Resposta")

    correct = models.BooleanField(blank=False, default=False,
                                  help_text="Esta é a resposta correta?")

    def __str__(self):
        return self.texto_resposta

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"


class RespostaDiscursiva(models.Model):
    """
    Reposta possívei para uma Questão discursiva

    questao (fk) - Id da QuestãoDiscursiva a qual essa resposta pertence.
    texto_resposta - O texto da resposta.
    """
    questao = models.OneToOneField(QuestaoDiscursiva, verbose_name="Questao")

    texto_resposta = models.CharField(max_length=1000,
                                      blank=False, null=False,
                                      help_text="Insira o texto da resposta.",
                                      verbose_name="Texto da Resposta")

    def __str__(self):
        return self.texto_resposta

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
