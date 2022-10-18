from math import *
from numpy import *
from random import uniform

# ----------------- DADOS-BASE PARA O CÓDIGO ------------------
    # robo
vR = 2.8 # m/s
aR = 2.8 # m/s^2
mR = 2.8 # kg

    # bola
mB = 0.046 # kg

rI = 0.001 # m 

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

trobo = []      # vai armazenar o tempo do robo
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

x = 0       # posição X da bolinha na interceptação
y = 0       # posição Y da bolinha na interceptação
d_max = 0       # distância percorrida pelo robo até a interceptação
d_min = 0       # distância percorrida pelo robo até a interceptação
t_desloc_max = 0        # tempo que o robô leva para interceptar a bola
t_desloc_min = 0        # tempo que o robô leva para interceptar a bola
ang_r = 0     # ângulo da movimentação do robô    
r_i = 0.1     # em (m) 

def pit (cat1, cat2):
    hip = sqrt(cat1*cat1 + cat2*cat2)
    return hip

for i in range(linha):
    x = posx[i]       # posição X da bolinha (percorre todas as posições possíveis, seguindo o tempo)
    y = posy[i]       # posição Y da bolinha                        ''
    d_max = pit(x - xirobo, y - yirobo)     # passa para a função cada X e Y da bolinha, tirando as posições X e Y iniciais do robo
    d_min = pit(x - r_i - xirobo, y - r_i - yirobo)     # passa para a função cada X e Y da bolinha, tirando as posições X e Y iniciais do robo
    t_desloc_max = d_max / 2.8          # calcula o tempo de deslocamento do robô até o ponto 
    t_desloc_min = (d_min - r_i) / 2.8

    if((t_desloc_min <= temp[i]) ):        # caso o robo consiga chegar nesse ponto em um tempo menor ou igual à bolinha -- a interceptação ocorre
        
        ang_r = degrees(arctan((y - r_i - yirobo)/(x - r_i - xirobo)))
        
        print("Interceptou!")
        break


print("interceptação -- posição x: %.3f, posição y: %.3f" %(x, y))
print("interceptação -- posição min x: %.3f, posição min y: %.3f" %(x - r_i, y - r_i))
print("tempo robo: %.3f, tempo bolinha: %.3f" %(t_desloc_max, temp[i]))
print("tempo mínimo %.3f" %t_desloc_min)
print("deslocamento max do robo: %.2f" %d_max)
print("deslocamento min do robo: %.2f" %d_min)
print("indice: %d" %(i+1))
print("ângulo: %f" %ang_r)
print("\n")