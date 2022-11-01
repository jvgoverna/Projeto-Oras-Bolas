from math import *
from random import uniform
from tkinter import N
import matplotlib.pyplot as grafico

# ----------------- DADOS-BASE PARA O CÓDIGO ------------------
    # robo
vR = 0 # m/s
aR = 2.8 # m/s^2
mR = 2.8 # kg

    # bola
mB = 0.046 # kg

# ----------- MANIPULAÇÃO DO ARQUIVO TXT EM VETORES -----------
temp = []
posx = []
posy = []

linha = -1       # variável que vai guardar a quantidade de linhas do arquivo -- inicializa no -1 para não contar a primeira linha do arquivo (t\s...)
for indice in open("trajetoria_bola_diurno.txt", "r"):
    if linha == -1:     # caso o laço esteja na primeira vez -- que seria a 1ª linha do arq (t\s...) ele não adiciona nada nas listas
        pass
    else:   # caso linha = 0 (já passou da primeira linha do arq) -- ele entra no laço
        indice = [i for i in indice.split()]
        temp.append(float(indice[0]))       # coloca o item da 1ª coluna no vetor de tempo
        posx.append(float(indice[1]))       # coloca o item da 2ª coluna no vetor da posição X
        posy.append(float(indice[2]))       # coloca o item da 3ª coluna no vetor da posição Y
    linha += 1


'''for i in range(linha):
    print("%.2f\t%.3f\t%.3f\t" %(temp[i], posx[i], posy[i]))'''

def velocidade (c1, c2, t1, t2):    # c1, c2 são coordenadas -- que vai variar se for X ou Y
    v = (c2 - c1) / (t2 - t1)
    return v

velXbolinha = []    # vai armazenar velocidade da bolinha em X
velYbolinha = []    # vai armazenar velocidade da bolinha em Y

for i in range(linha):
    if i == 0:
        velXbolinha.append(0)
        velYbolinha.append(0)
    else:
        velXbolinha.append(velocidade(posx[i-1], posx[i], temp[i-1], temp[i]))
        velYbolinha.append(velocidade(posy[i-1], posy[i], temp[i-1], temp[i]))

#for i in range(linha):
    #print("%.2f %.2f, indice: %d" %(velXbolinha[i], velYbolinha[i], i))    # verificação se a velocidade está sendo calculada direito

vrobo = []      # vai armazenar a velocidade do robo
varobo = []     # vai armazenar a velocidade de aceleração do robô
vdrobo = []     # vai armazenar a velocidade de desaceleração do robô
xrobo = []      # vai armazenar as posições x do robo
yrobo = []      # vai armazenar as posições y do robo

# ------------------- posição do robo --------------------

qtdt = 0        # contador para o array do tempo do robo
qtdv = 0        # contador para o array da velocidade do robo

xirobo = uniform(0, 2)           # posição x do robo inicial aleatória
yirobo = uniform(0, 1.5)         # posição y do robo incicial aleatória

xrobo.append(xirobo)            # adiciona a posição x inicial do robo no array das posições x
yrobo.append(yirobo)            # adiciona a posição y inicial do robo no array das posições y

print("X do Robo: %.2f" % xirobo)     # printar o x e o y inicial do robo
print("Y do Robo: %.2f" % yirobo)     # printar o x e o y inicial do robo

# --------------- cálculo da interceptação ---------------

    # variáveis da interceptação

x = 0       # posição X da bolinha 
y = 0       # posição Y da bolinha 
vel = 0       # velocidade do robô que vai alterando até 2.8
vI = 0        # velocidade inicial do robô
x_int = 0     # posição X da bolinha na interceptação
y_int = 0     # posição Y da bolinha na interceptação
d_max = 0       # distância percorrida pelo robo até a interceptação
d_min = 0       # distância percorrida pelo robo até a interceptação
d1 = 0           # menor distância até a interceptação
d2 = 0           # menor distância até a interceptação
t_desloc_max = 0        # tempo que o robô leva para interceptar a bola
t_desloc_min = 0        # tempo que o robô leva para interceptar a bola
ang_r = 0     # ângulo da movimentação do robô    
ang_b = 0     # ângulo da movimentação da bolinha  
r_i = 0.01     # em (m) 
t_ac = 0
t_des = 0
t_total = 0
t_const = 0
d_ac = 0
d_des = 0
d_const = 0
d_total = 0
v_ac = 0

varobo.append(vel)      #coloca a primeira velocidade do robô dentro do array

def pit (cat1, cat2):
    hip = cat1*cat1 + cat2*cat2
    return sqrt(hip)

for i in range(linha):
    x = posx[i]       # posição X da bolinha (percorre todas as posições possíveis, seguindo o tempo)
    y = posy[i]       # posição Y da bolinha  

    if vel < 2.8:
        vel = vI + aR * 0.02
        vI = vel
        vR = vel
        varobo.append(vR)
    
    if(y > 6):      # para que o robô não intercepte a bolinha fora do campo
        pass
    else:            
        d1 = pit(x - xirobo, y - yirobo)     # passa para a função cada X e Y da bolinha, tirando as posições X e Y iniciais do robo
        d2 = pit(x - r_i - xirobo, y - r_i - yirobo)     # passa para a função cada X e Y da bolinha, tirando as posições X e Y iniciais do robo
        
        if (d1 < d2):
            d_min = d1
            d_max = d2
            x_int = x
            y_int = y
        else:
            d_min = d2
            d_max = d1
            x_int = x - r_i
            y_int = y - r_i 
        
        t_desloc_max = sqrt((2 * d_max) / aR)        # calcula o tempo de deslocamento do robô até o ponto 
        t_desloc_min = sqrt((2 * d_min) / aR)        # guarda o tempo que leva para interceptar a bolinha

    if d_min <= 2.8:
        d_total = d_min             # só tem a mudança de variável  
        d_ac = d_total / 2          # como não tem o alcançe da velocidade máxima, não tem período de velocidade constante, 
                                    # então a distância que ele percorre para acelerar é a metade da total
        d_des = d_ac                # a distância de aceleração é a mesma de desaceleração, porque o tempo para as duas é o mesmo

        t_ac = sqrt((2 * d_ac) / aR)      # delta S = Vo*t + ((a*t**2)/2)
        t_des = t_ac
        t_total = 2 * t_ac

        v_ac = sqrt(d_ac * 2 * aR)      # velocidade final do robô caso ele não chegue a 2.8 m/s

        vrobo.append(vR)
    else:
        d_total = d_min
        d_ac = 1.4          # como a ace é máxima, a distância que ele usa pra alcançar a velocidade máxima é sempre de 1.4 m
        t_ac = 1            # o robô leva 1s para alcançar a velocidade máxima -- considerando aMáx

        # calculando a distância que o robô percorre em velocidade constante
        d_const = d_total - (2 * d_ac)      # dist de desaceleração é a mesma da aceleração, por isso x2

        t_const = sqrt((2 * d_const) / aR)  # tempo em que a velocidade do robô permanece constante

        t_total = (2 * t_ac) + t_const      # deltaS = Vot + (at**2)/2

        v_ac = sqrt(d_ac * 2 * aR)

    if  t_total <= temp[i]:
        ang_r = degrees(atan((y_int - yirobo)/(x_int - xirobo)))
        ang_b = degrees(atan((y_int - posy[0])/(x_int - posx[0])))
        print("interceptou")
        break

print("posição máxima: (%.3f, %.3f)" %(x, y))
print("posição min: (%.3f, %.3f)" %(x - r_i, y - r_i))
print("tempo máx robo: %.3f, tempo bolinha: %.3f" %(t_desloc_max, temp[i]))
print("tempo mínimo %.3f" %t_desloc_min)
print("deslocamento max do robo: %.5f" %d_max)
print("deslocamento min do robo: %.5f" %d_min)
print("velocidade inicial do robô: %.2f" %vI)
print("velocidade final do robô: %.2f" %vel)
print("velocidade interceptação do robô: %.2f" %vR)
print("tempo de aceleração do robô: %.2f" %t_ac)
print("tempo de desaceleração do robô: %.2f" %t_des)
print("tempo na v constante do robô: %.5f" %t_const)
print("tempo total do robô: %.2f" %t_total)
print("deslocamento de aceleração do robô: %.5f" %d_ac)
print("deslocamento total do robô: %.5f" %d_total)
print("deslocamento de desaceleração do robô: %.5f" %d_des)
print("deslocamento na v constante do robô: %.5f" %d_const)
print("velocidade final do robô: %.2f" %v_ac)
print("indice: %d" %(i+1))
print("ângulo do robô: %f" %ang_r)
print("ângulo da bolinha: %f" %ang_b)

# ------------------------------ GOL -----------------------------------

xgd = 9.0           # X do gol da direita
ygd = 3.0           # Y do gol da direita
xge = 0             # X do gol da esquerda
yge = 3.0           # Y do gol da esquerda
dc = 0              # distância do chute até o gol
ang_c = 0           # ângulo do chute até o gol

if x_int >= 4.5:                           # se o X da interceptação for maior ou igual a 4.5 (metade do campo)
    dc = pit(xgd - x_int, ygd - y_int)
    ang_c = degrees(atan((ygd - y_int)/(xgd - x_int)))
    print("Gol da direita")
    
elif x_int < 4.5:                          # se o Y da interceptação for menor que 4.5 (metade do campo)
    dc = pit(xge - x_int, yge - y_int)
    ang_c = degrees(atan((yge - y_int)/(xge - x_int)))
    print("Gol da esquerda")

'''print("Distância percorrida pela bola até o gol: %.2f" % dc)
print("Ângulo da bola até o gol: %.2f" % ang_c)
print("Coordenadas da interceptação: (%.2f, %.2f)" %(x_int, y_int))'''
print("\n")

# ------------------- CRIAÇÃO DOS VETORES -------------------

#   criação de variáveis 
vXrobo = []
vYrobo = []
aXrobo = 2.8 * cos(radians(ang_r))
aYrobo = 2.8 * sin(radians(ang_r))

modulo_ti = t_const / 0.02

vrobo = varobo

for i in range(int(modulo_ti)):
    vrobo.append(2.8)

for i in varobo[::-1]:
    if i == vrobo[-1]:
        pass
    else:
        vrobo.append(i)

for i in range(len(vrobo)):
    print('%.3f' %vrobo[i], end=" ")

print("\n")
if ang_r < 0:
    ang_r = ang_r * (-1)
else:
    pass

for i in range(len(vrobo)):
    vXrobo.append(float(vrobo[i]) * cos(radians(ang_r)))

for i in range(len(vrobo)):
    vYrobo.append(float(vrobo[i]) * sin(radians(ang_r)))

#for i in range(len(vrobo)):
    #print('%.3f' %vYrobo[i], end=" ")

temp_int = []

for i in range(len(vXrobo)):
    temp_int.append(temp[i])

print(vXrobo)
print(vYrobo)

grafico.ylabel("velocidade x(m)")
grafico.xlabel("Tempo (s)")
grafico.axis(ymin = 0, ymax=7)
grafico.axis(xmin = 0, xmax = 7)

grafico.title("Velocidade X do robo em função do tempo até a interceptação")
grafico.plot(temp_int,vXrobo)
grafico.show()



grafico.ylabel("velocidade Y(m)")
grafico.xlabel("Tempo (s)")
grafico.axis(ymin = 0, ymax=7)
grafico.axis(xmin = 0, xmax = 7)

grafico.title("Velocidade Y do robo em função do tempo até a interceptação")
grafico.plot(temp_int,vYrobo)
grafico.show()
