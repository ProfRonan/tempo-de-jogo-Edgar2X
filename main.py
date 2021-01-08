"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI

from datetime import time

hora_inicio = input("")
hour, min,second  = [int(i) for i in hora_inicio.split(":")]
hora_termino = input("")
hour1, min1,second1 = [int(i) for i in hora_termino.split(":")]

min_f = min1 - min
hour_f = hour1 - hour
second_f = second1 - second

if second_f == 00 and min_f == 0 and hour_f == 0:
  hour_f = 24 

i=0
if second_f < 0:
  second_f = 60 + second_f
  i = 1 
  if second_f < 10:
    second_f = f'0{second_f}'
elif second_f < 10:
    second_f = f'0{second_f}'

i2=0
if min_f < 0:
  min_f = 60 + min_f - i
  i2 = 1
  if min_f < 10:
    min_f = f'0{min_f}'
elif min_f < 10:
  min_f = f'0{min_f}'
else:
  min_f = min_f - i

if hour_f < 0:
  hour_f = 24 + hour_f - i2
  if hour_f < 10:
    hour_f = f'0{hour_f - i2}'
elif hour_f < 10:
  hour_f = f'0{hour_f - i2}'
else: 
  hour_f - i2


print(f'{hour_f}:{min_f}:{second_f}')

if __name__ == '__main__':
    main()
