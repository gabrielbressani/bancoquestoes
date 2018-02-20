from rest_framework import serializers

from questoes.models import QuestaoObjetiva, QuestaoDiscursiva, Resposta, RespostaDiscursiva


class RespostaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Resposta
        fields = ('id', 'texto_resposta', 'correct')


class QuestaoObjetivaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    resposta_set = RespostaSerializer(many=True)

    def create(self, validated_data):
        resposta_set = validated_data.pop('resposta_set')
        questao = QuestaoObjetiva.objects.create(**validated_data)

        for resp in resposta_set:
            Resposta.objects.create(questao=questao, **resp)

        return questao

    def update(self, instance, validated_data):
        """
        Método que atualiza uma instância de uma questão objetiva e suas Repostas.

        :param instance: instancia atual da entidade
        :param validated_data: valor validado
        :return: a instância de Questão Objetiva e sua Respostas atualizadas
        """
        resposta_set_data = validated_data.pop('resposta_set')
        respostas_map = {resposta.id: resposta for resposta in instance.resposta_set.all()}
        data_map = {resp['id']: resp for resp in resposta_set_data}

        for data_id, data in data_map.items():
            resposta = respostas_map.get(data_id, None)

            if resposta is None:
                Resposta.objects.create(questao=instance, **data)
            else:
                print(data_id)
                filtered = Resposta.objects.filter(id=data_id)
                print(filtered)
                filtered.update(**data)

        for resposta_id, resposta in respostas_map.items():
            if resposta_id not in data_map:
                resposta.delete()

        instance.texto_questao = validated_data.get('texto_questao', instance.texto_questao)
        instance.save()

        return instance

    class Meta:
        model = QuestaoObjetiva
        fields = ('id', 'texto_questao', 'resposta_set')


class RespostaDiscursivaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RespostaDiscursiva
        fields = ('id', 'texto_resposta')


class QuestaoDiscursivaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    respostadiscursiva = RespostaDiscursivaSerializer()

    def create(self, validated_data):
        respostadiscursiva = validated_data.pop('respostadiscursiva')
        questao = QuestaoDiscursiva.objects.create(**validated_data)
        RespostaDiscursiva.objects.create(questao=questao, **respostadiscursiva)

        return questao

    class Meta:
        model = QuestaoDiscursiva
        fields = ('id', 'texto_questao', 'respostadiscursiva')
