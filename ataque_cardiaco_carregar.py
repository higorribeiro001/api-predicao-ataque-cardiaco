import numpy as np
from keras.models import model_from_json

def rede_neural(novo):
    arquivo = open('classificador.json', 'r')
    
    estrutura_rede = arquivo.read()
    arquivo.close()
    
    classificador = model_from_json(estrutura_rede)
    classificador.load_weights('classificador.weights.h5')
    
    novo = np.array([novo])
    
    previsao = classificador.predict(novo)
    
    return previsao

# print(rede_neural([45, 1, 3, 130, 250, 0, 1, 175, 0, 2.3, 0, 2, 2]))

# age: 45 (Idade)
# sex: 1 (Sexo: 1 para masculino, 0 para feminino)
# cp: 3 (Tipo de dor no peito: 0-3)
# trtbps: 130 (Pressão arterial em repouso)
# chol: 250 (Colesterol sérico)
# fbs: 0 (Açúcar no sangue em jejum > 120 mg/dl: 1 = verdadeiro, 0 = falso)
# restecg: 1 (Resultados do eletrocardiograma em repouso: 0-2)
# thalachh: 175 (Frequência cardíaca máxima alcançada)
# exng: 0 (Angina induzida por exercício: 1 = sim, 0 = não)
# oldpeak: 2.3 (Depressão de ST induzida pelo exercício em relação ao repouso)
# slp: 0 (Inclinação do segmento ST do exercício de pico: 0-2)
# caa: 2 (Número de vasos principais coloridos por fluoroscopia: 0-3)
# thall: 2 (Thal: 1 = normal, 2 = defeito fixo, 3 = defeito reversível)
# output: 1 (Resultado: 1 = doença cardíaca presente, 0 = ausência de doença cardíaca)
