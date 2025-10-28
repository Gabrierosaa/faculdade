import random as r
import statistics as s
import datetime as d

clts = ["Gustavo", "Vitor", "Joao", "Maria", "Igor", "Julia", "Matheus", "Alana"]
notas = r.sample(range(0, 11), len(clts))
media = 0
    
for i in range(len(clts)):
    print(clts[i], "Nota:",notas[i])

for i in range(len(notas)):
    media = media + notas[i]


mediaprint = media / 8
data = d.date.today()
mediana = s.median(notas) 
maior = max(notas)
menor = min(notas)
aluno_maior = clts[notas.index(maior)]
aluno_menor = clts[notas.index(menor)]
print(f"""
=========================================
|A Media foi {mediaprint} | {data}       
|A mediana foi {mediana} | {data}        
|A Maior nota foi {aluno_maior} | {data} 
|A menor nota foi {aluno_menor} | {data} 
=========================================
""")
