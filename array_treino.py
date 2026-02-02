import numpy as np
import pandas as pd
import os
'''
teste1 = np.array([3.14, 4, 2, 3]) #só aceita um  tipo de dado se diferente ele mudar todos para unificar


#dtype altera o tipo dos dados presente na array
teste2 = np.array([1, 2, 3, 4], dtype='float32') #np 

teste3 = np.array([range(i, i + 3) for i in [2, 4, 6]])
teste4 = np.zeros(10, dtype=int)
teste5 = np.random.randint(0, 10, (3, 3))
print(teste1)
print(teste2)
print(teste3)
print(teste4)
print(teste5)
'''
caminho_arquivo = r"C:\Users\franc\Documents\Faculdade\Python\aprendendo_numpy"
nome_arquivo = "dados_presidente.csv"
caminho_completo = os.path.join(caminho_arquivo, nome_arquivo)


data = pd.read_csv(caminho_completo, sep=';')

heights = np.array(data['height(cm)'])
#print(heights)
#print("Mean height: ", heights.mean())
df=data
print(df)

print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())