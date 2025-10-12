from classes.Receita import Receita
from classes.Remedio import Remedio

receita = Receita("12-10-2025",[Remedio("dorflex","1g",[1,3,2], 12), Remedio("paracetamol","400mg",[4,2,1], 20)])
# 1 unidade pra ingerir,3 comprimidos a cada 2 dias 
# [1,3,2] 

remedios = receita.getRemedios()
for i in remedios:
    print(i.getNome())
