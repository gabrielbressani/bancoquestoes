import logging

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from questoes.forms import QuestaoObjetivaFormSet, QuestaoDiscursivaFormSet
from questoes.models import QuestaoObjetiva, QuestaoDiscursiva, Questao


logger = logging.getLogger(__name__)


class ListQuestoes(ListView):
    """
    Retorna a lista de Questoões completa ou filtrada por seus texto.
    """
    model = Questao

    def get_queryset(self):
        logger.info("Listando Questoes")
        q = self.request.GET.get('q', '')
        if q:
            logger.info("Filtrando Questoes por {}".format(q))
            return Questao.objects.filter(texto_questao__contains=q).select_subclasses()

        return Questao.objects.all().select_subclasses()


"""
Abaixo as views para manipular as ações 
das Questoes Objetivas e suas Respostas
"""


class CreateQuestaoObjetiva(CreateView):
    """
    Cria Questão objetiva
    """
    model = QuestaoObjetiva
    fields = ['texto_questao']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Criando Questão Objetiva")
        return super(CreateQuestaoObjetiva, self).dispatch(*args, **kwargs)


class UpdateQuestaoObjetiva(UpdateView):
    """
    Atualiza Questão Objetiva
    """
    model = QuestaoObjetiva
    success_url = '/'
    fields = ['texto_questao']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Atualizando Questão Objetiva")
        return super(UpdateQuestaoObjetiva, self).dispatch(*args, **kwargs)


class DeleteQuestaoObjetiva(DeleteView):
    """
    Remove Questão Objetiva
    """
    model = QuestaoObjetiva
    success_url = reverse_lazy('questoes-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Removendo Questão Objetiva")
        return super(DeleteQuestaoObjetiva, self).dispatch(*args, **kwargs)


class CreateResposta(CreateView):
    """
    Cria uma coleção de Respostas para a Questão Objetiva
    """
    model = QuestaoObjetiva
    fields = ['texto_questao']
    success_url = reverse_lazy('questoes-list')

    def get_context_data(self, **kwargs):
        data = super(CreateResposta, self).get_context_data(**kwargs)

        if self.request.POST:
            data['respostas'] = QuestaoObjetivaFormSet(self.request.POST)
        else:
            data['respostas'] = QuestaoObjetivaFormSet()

        return data

    def form_valid(self, form):
        logger.info("Validando Criação Resposta")
        context = self.get_context_data()
        respostas = context['respostas']

        with transaction.atomic():
            self.object = form.save()

            if respostas.is_valid():
                respostas.instance = self.object
                respostas.save()

        return super(CreateResposta, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Crinado Resposta")
        return super(CreateResposta, self).dispatch(*args, **kwargs)


class UpdateResposta(UpdateView):
    """
    Atualiza uma coleção de Respostas para a Questão Objetiva
    """
    model = QuestaoObjetiva
    fields = ['texto_questao']
    success_url = reverse_lazy('questoes-list')

    def get_context_data(self, **kwargs):
        data = super(UpdateResposta, self).get_context_data(**kwargs)
        if self.request.POST:
            data['respostas'] = QuestaoObjetivaFormSet(self.request.POST, instance=self.object)
        else:
            data['respostas'] = QuestaoObjetivaFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        respostas = context['respostas']

        with transaction.atomic():
            self.object = form.save()

            if respostas.is_valid():
                respostas.instance = self.object
                respostas.save()

        return super(UpdateResposta, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Atualizando Resposta")
        return super(UpdateResposta, self).dispatch(*args, **kwargs)


"""
Abaixo as views para manipular as ações 
das Questoes Discursivas e a sua Resposta
"""


class CreateQuestaoDiscursiva(CreateView):
    """
    Cria Questão Discursiva
    """
    model = QuestaoDiscursiva
    fields = ['texto_questao']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Criando Questão Discursiva")
        return super(CreateQuestaoDiscursiva, self).dispatch(*args, **kwargs)


class UpdateQuestaoDiscursiva(UpdateView):
    """
    Atualiza Questão Discursiva
    """
    model = QuestaoDiscursiva
    success_url = '/'
    fields = ['texto_questao']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Atualizando Questão Discursiva")
        return super(UpdateQuestaoDiscursiva, self).dispatch(*args, **kwargs)


class DeleteQuestaoDiscursiva(DeleteView):
    """
    Remove Questão Discursiva
    """
    model = QuestaoDiscursiva
    success_url = reverse_lazy('questoes-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Deletando Questão Discursiva")
        return super(DeleteQuestaoDiscursiva, self).dispatch(*args, **kwargs)


class CreateRespostaDiscursiva(CreateView):
    """
    Cria uma Resposta Discursiva para uma Questão Discursiva
    """
    model = QuestaoDiscursiva
    fields = ['texto_questao']
    success_url = reverse_lazy('questoes-list')

    def get_context_data(self, **kwargs):
        data = super(CreateRespostaDiscursiva, self).get_context_data(**kwargs)

        if self.request.POST:
            data['respostas'] = QuestaoDiscursivaFormSet(self.request.POST)
        else:
            data['respostas'] = QuestaoDiscursivaFormSet()

        return data

    def form_valid(self, form):
        logger.info("Validando Resposta Discursiva")
        context = self.get_context_data()
        respostas = context['respostas']

        with transaction.atomic():
            self.object = form.save()

            if respostas.is_valid():
                respostas.instance = self.object
                respostas.save()

        return super(CreateRespostaDiscursiva, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        logger.info("Criando Resposta Discursiva")
        return super(CreateRespostaDiscursiva, self).dispatch(*args, **kwargs)


class UpdateRespostaDiscursiva(UpdateView):
    """
    Atualiza uma Resposta Discursiva para uma Questão Discursiva
    """
    model = QuestaoDiscursiva
    fields = ['texto_questao']
    success_url = reverse_lazy('questoes-list')

    def get_context_data(self, **kwargs):
        data = super(UpdateRespostaDiscursiva, self).get_context_data(**kwargs)
        if self.request.POST:
            data['respostas'] = QuestaoDiscursivaFormSet(self.request.POST, instance=self.object)
        else:
            data['respostas'] = QuestaoDiscursivaFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        logger.info("Validando Autalização Resposta Discursiva")
        context = self.get_context_data()
        respostas = context['respostas']

        with transaction.atomic():
            self.object = form.save()

            if respostas.is_valid():
                respostas.instance = self.object
                respostas.save()

        return super(UpdateRespostaDiscursiva, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateRespostaDiscursiva, self).dispatch(*args, **kwargs)
