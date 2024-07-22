from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Heart
from .serializers import HeartSerializer, HeartAttackPredictionSerializer
from rest_framework.response import Response
from rest_framework import status
from ataque_cardiaco_carregar import rede_neural
from drf_spectacular.utils import extend_schema, OpenApiRequest, OpenApiResponse

class PossibilityAttackAPIv1ViewSet(ModelViewSet):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    pagination_class = PageNumberPagination

    @extend_schema(
        request=HeartAttackPredictionSerializer,
        description='''
            Ao realizer o registro, os dados serão salvos no banco junto ao resultado e será exibido o resultado como resposta. 
            Clique em "Schema" para saber mais detalhes de como enviar os dados. 
            Mas, para ajudar, também deixarei disponível aqui:
            "age" é "Idade", "sex" é "Sexo" (1: masculino; 0: feminino), "cp" é "Tipo de dor no peito" (1: angina típica; 2: angina atípica; 3: dor não anginosa; 4: assintomático),
            "trtbps" é "Pressão arterial em repouso" (Inteiro, mm Hg), "chol" é "Colesterol sérico" (Inteiro, mg/dl), 
            "fbs" é "Glicemia de jejum" > 120 mg/dl (categórico; 1 = verdadeiro, 0 = falso), 
            "restecg" é "Resultados eletrocardiográficos em repouso" (0: normal; 1: Anormalidade da onda ST-T; 2: hipertrofia ventricular esquerda provável ou definitiva),
            "thalachh" é "Frequência cardíaca máxima alcançada" (Inteiro),
            "exng" é "Angina induzida por exercício" (categórico; 1 = sim, 0 = não),
            "oldpeak" é "Depressão do segmento ST induzida pelo exercício em relação ao repouso" (Decimal),
            "slp" é "Inclinação do segmento ST do exercício de pico" (1: ascendente; 2: plano; 3: declive),
            "caa" é "Número de vasos principais coloridos por fluoroscopia": 0-3
            "thall" é "Talassemia" (3: normal; 6: defeito corrigido; 7: defeito reversível),
            "user_id" é o "id" do usuário (pode ser encontrado na lista de usuários)''',
        responses=OpenApiResponse(description="Previsão do ataque cardíaco")
    )

    def create(self, request, *args, **kwargs):
        try:
            params = [
                request.data['age'],
                request.data['sex'],
                request.data['cp'],
                request.data['trtbps'],
                request.data['chol'],
                request.data['fbs'],
                request.data['restecg'],
                request.data['thalachh'],
                request.data['exng'],
                request.data['oldpeak'],
                request.data['slp'],
                request.data['caa'],
                request.data['thall'],
            ]

            output = 1 if rede_neural(params)[0][0] > 0.5 else 0

            request.data.update(
                {
                    'output': output
                }
            )

            serializer = HeartSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

            if output == 1:
                output = 'Grande chance de sofrer um infarto, doença cardíaca presente, vá ao médico, priorize a sua saúde.'
            else:
                output = 'Pouca chance de sofrer um infarto, doença cardíaca ausente, mas não deixe de realizer consultas.'

            return Response(output, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)