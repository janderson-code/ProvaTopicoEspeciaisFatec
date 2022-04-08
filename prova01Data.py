import os
from datetime import date

os.system("clear")

dataAtual = date.today()
diaAtual = dataAtual.day
mesAtual = dataAtual.month
anoAtual = dataAtual.year

dataDiaMesAno = dataAtual.strftime("%d/%m/%y")
dataFormatMesExtenso = dataAtual.strftime("%d/%B/%y")

print(f"Data atual {dataAtual}\nDiaAtual : {diaAtual}\nMês Atual : {mesAtual}\nAno: {anoAtual}\nData Formatada {dataDiaMesAno}\nData com Mês por Extenso {dataFormatMesExtenso}")
