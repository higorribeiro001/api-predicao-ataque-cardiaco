from rest_framework import serializers
from .models import Heart

class HeartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Heart
        fields=('__all__')

    user = serializers.StringRelatedField(
		source='user_id',
	)

class HeartAttackPredictionSerializer(serializers.Serializer):
    age = serializers.IntegerField(required=True, help_text='Idade')
    sex = serializers.IntegerField(required=True, help_text='Sexo (1: masculino; 0: feminino)')
    cp = serializers.IntegerField(required=True, help_text='Tipo de dor no peito (1: angina típica; 2: angina atípica; 3: dor não anginosa; 4: assintomático)')
    trtbps = serializers.IntegerField(required=True, help_text='Pressão arterial em repouso (Inteiro, mm Hg)')
    chol = serializers.IntegerField(required=True, help_text='Colesterol sérico (Inteiro, mg/dl)')
    fbs = serializers.IntegerField(required=True, help_text='Glicemia de jejum > 120 mg/dl (categórico; 1 = verdadeiro, 0 = falso)')
    restecg = serializers.IntegerField(required=True, help_text='Resultados eletrocardiográficos em repouso (0: normal; 1: Anormalidade da onda ST-T; 2: hipertrofia ventricular esquerda provável ou definitiva)')
    thalachh = serializers.IntegerField(required=True, help_text='Frequência cardíaca máxima alcançada (Inteiro)')
    exng = serializers.IntegerField(required=True, help_text='Angina induzida por exercício (categórico; 1 = sim, 0 = não)')
    oldpeak = serializers.FloatField(required=True, help_text='Depressão do segmento ST induzida pelo exercício em relação ao repouso (Decimal)')
    slp = serializers.IntegerField(required=True, help_text='Inclinação do segmento ST do exercício de pico (1: ascendente; 2: plano; 3: declive)')
    caa = serializers.IntegerField(required=True, help_text='Número de vasos principais coloridos por fluoroscopia: 0-3')
    thall = serializers.IntegerField(required=True, help_text='Talassemia (3: normal; 6: defeito corrigido; 7: defeito reversível)')
    user_id = serializers.IntegerField(required=True, help_text='Digite o "id" do usuário que pode ser encontrado na lista de usuários')
