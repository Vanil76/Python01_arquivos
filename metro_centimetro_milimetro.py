from funcoes import *

num = float(input('Digite um valor em metros: '))
milimetro = metro_mm(num)
centimetro = metro_cent(num)
print(f'{num}m² convertido em centímentros são {centimetro}cm ')
print(f'{num}m² convertido em milímetros são {milimetro}mm ')
