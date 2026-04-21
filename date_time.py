from datetime import date, datetime

data = date(2026, 8, 20)
print(data)
print(data.year)
print(data.today())

date_hora = datetime(2026, 8, 25)
print(date_hora)
print(datetime.today())
#///////////////////////////////////////////////////////////////////////////#
import datetime

d = datetime.datetime(2026, 8, 25, 15, 30,45)
print(d)

d = d + datetime.timedelta(weeks=2, days=5, hours=3, minutes = 30, seconds=15)
print(d)
#///////////////////////////////////////////////////////////////////////////#
from datetime import date, datetime, time, timedelta 

tipo_carro = "P" #P, M, G 
tempo_pequeno = 30
tempo_medio = 60
tempo_grande = 90
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"o carro chegou: {data_atual} e ficara pronto as: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"o carro chegou: {data_atual} e ficara pronto as: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"o carro chegou: {data_atual} e ficara pronto as: {data_estimada}")

print(date.today() - timedelta(days= 7,))