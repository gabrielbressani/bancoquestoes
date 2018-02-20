from django import forms
from django.forms import inlineformset_factory

from questoes.models import QuestaoObjetiva, Resposta, QuestaoDiscursiva, RespostaDiscursiva


class QuestaoObjetivaForm(forms.ModelForm):

    class Meta:
        model = QuestaoObjetiva
        exclude = ()


class RespostaForm(forms.ModelForm):

    class Meta:
        model = Resposta
        exclude = ()


class QuestaoDiscursivaForm(forms.ModelForm):

    class Meta:
        model = QuestaoDiscursiva
        exclude = ()


class RespostaDiscursivaForm(forms.ModelForm):

    class Meta:
        model = RespostaDiscursiva
        exclude = ()


QuestaoObjetivaFormSet = inlineformset_factory(QuestaoObjetiva, Resposta, form=RespostaForm, extra=1)
QuestaoDiscursivaFormSet = inlineformset_factory(QuestaoDiscursiva, RespostaDiscursiva, form=RespostaDiscursivaForm, extra=1)


