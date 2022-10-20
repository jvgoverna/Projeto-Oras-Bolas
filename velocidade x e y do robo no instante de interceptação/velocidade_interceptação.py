from math import *
from numpy import *
from random import uniform
temp =[]
posx =[]
posy =[]
linha = -1
for indice in open("trajetoria_bola_diurno.txt","r"):
    if linha == -1:
        pass
    else:
        indice = [i for i in indice.split()]
        temp.append(float(indice[0]))       # coloca o item da 1ª coluna no vetor de tempo
        posx.append(float(indice[1]))       # coloca o item da 2ª coluna no vetor da posição X
        posy.append(float(indice[2]))       # coloca o item da 3ª coluna no vetor da posição Y
    linha += 1


velXbolinha = []
velYbolinha = []


def velocidade (c1, c2, t1, t2):    # c1, c2 são coordenadas -- que vai variar se for X ou Y
    v = (c2 - c1) / (t2 - t1)
    return v

for i in range(linha):
    if i == 0:
        velXbolinha.append(0)
        velYbolinha.append(0)
    else:
        velXbolinha.append(velocidade(posx[i-1], posx[i], temp[i-1], temp[i]))
        velYbolinha.append(velocidade(posy[i-1], posy[i], temp[i-1], temp[i]))

#for i in range(linha):
    #print("%.2f %.2f, indice: %d" %(velXbolinha[i], velYbolinha[i], i))


# ------------------- posição do robo --------------------
xrobo =[]
yrobo = []

xirobo = uniform(0,2) #Xinicial do robo
yirobo = uniform (0,1.5) #Y inicial do robo
xrobo.append(xirobo)
yrobo.append(yrobo)
print("X do Robo: %.2f" % (xirobo))
print("Y do Robo: %.2f" % (yirobo))

# --------------- cálculo da interceptação ---------------

    # variáveis da interceptação

x = 0       # posição X da bolinha 
y = 0       # posição Y da bolinha 
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
vR = 2.8

def pit (cat1, cat2):
    hip = cat1*cat1 + cat2*cat2
    return sqrt(hip)

for i in range(linha):
    x = posx[i]       # posição X da bolinha (percorre todas as posições possíveis, seguindo o tempo)
    y = posy[i]       # posição Y da bolinha                        ''
    
    if(y > 6):      # para que o robô não intercepte a bolinha fora do campo
        pass
    else:            
        d1 = pit(x - xirobo, y - yirobo)     # passa para a função cada X e Y da bolinha, tirando as posições X e Y iniciais do robo #max
        d2 = pit(x - r_i - xirobo, y - r_i - yirobo)     # passa para a função cada X e Y da bolinha, tirando as posições X e Y iniciais do robo #min

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

        t_desloc_max = d_max / vR          # calcula o tempo de deslocamento do robô até o ponto 
        t_desloc_min = d_min / vR          # guarda o tempo que leva para interceptar a bolinha

        if((t_desloc_min <= temp[i]) ):        # caso o robo consiga chegar nesse ponto em um tempo menor ou igual à bolinha -- a interceptação ocorre
            
            ang_r = degrees(arctan((y_int - yirobo)/(x_int - xirobo)))
            ang_b = degrees(arctan((y_int - posy[0])/(x_int - posx[0])))
            print("Interceptou!")
            break


print("posição máxima: (%.3f, %.3f)" %(x, y))
print("posição min: (%.3f, %.3f)" %(x - r_i, y - r_i)) #do robo
print("tempo robo: %.3f, tempo bolinha: %.3f" %(t_desloc_max, temp[i]))
print("tempo mínimo %.3f" %t_desloc_min)
print("deslocamento max do robo: %.2f" %d_max)
print("deslocamento min do robo: %.2f" %d_min)
print("indice: %d" %(i+1))
print("ângulo do robô: %f" %ang_r)
print("ângulo da bolinha: %f" %ang_b)
print("\n")

# ------------------------------ GOL -----------------------------------

xgd = 9.0           # X do gol da direita
ygd = 3.0           # Y do gol da direita
xge = 0             # X do gol da esquerda
yge = 3.0           # Y do gol da esquerda
dc = 0              # distância do chute até o gol
ang_c = 0           # ângulo do chute até o gol


if x_int >= 4.5:                           # se o X da interceptação for maior ou igual a 4.5 (metade do campo)
    dc = pit(xgd - x_int, ygd - y_int)
    ang_c = degrees(arctan((ygd - y_int)/(xgd - x_int)))
    print("Gol da direita")
    
elif x_int < 4.5:                          # se o Y da interceptação for menor que 4.5 (metade do campo)
    dc = pit(xge - x_int, yge - y_int)
    ang_c = degrees(arctan((yge - y_int)/(xge - x_int)))
    print("Gol da esquerda")

print("Distância percorrida pela bola até o gol: %.2f" % dc)
print("Ângulo da bola até o gol: %.2f" % ang_c)
print("Coordenadas da interceptação: (%.2f, %.2f)" %(x_int, y_int))
print("\n")


vRseg = 0.058 #Velocidade do robo a cada 0.02s

vx = vRseg * sin(ang_r)
print("Velocidade em x = %.3f" %(vx))

vy = vRseg * cos(ang_r)
print("Velocidade em Y = %.3f" %(vy))

#fazer um for com base a trajetoria_diurno.txt percorrendo todos os pontos x e y até o instante de interceptação!

arquivo1 = open("trajetoria_bola_diurno.txt","r") #abri o arquivo da trajetória da bola 
arquivo2 = open("posição x e y da bolinha até o momento de interceptação.txt","w+") # abri um novo arquivo com base na trajetória da bola 

linha_arquivo1 = arquivo1.readlines() #variável que lerá todos os items do txt da trajetória da bola 
for linha in linha_arquivo1: # laço para alterar oq será escrito no novo txt
    if linha == linha_arquivo1[0]: # pulará a primeira linha do arquivo (t,x,y)
        continue
    arquivo2.write(linha) #escreverá no novo arquivo
    linhaformatada = linha.split() 
    tempo = float(linhaformatada[0]) #passará os dados de int para float
    if tempo >= t_desloc_min: # se o tempo em 0.02s for maior ou igual ao tempo do deslocamento mínimo parará o laço e fechará os dois arquivos.
        arquivo1.close()
        arquivo2.close()
        break

posxBol = []
posyBol = []

arquivo2 = open("posição x e y da bolinha até o momento de interceptação.txt","r")
arquivo2_linhas = arquivo2.readlines()
for linhas in arquivo2_linhas:
    linhaformatada2 = linhas.split()
    posxBol.append(linhaformatada2[1])
    posyBol.append(linhaformatada2[2])
arquivo2.close()

print(posxBol)
print(posyBol)



k = int(t_desloc_min/0.02)

for i in range(k):
    delta_x = (x - r_i) - (xirobo)
    total_x = delta_x * 0.02 + x-r_i * t_desloc_min
print("Posição X do robo até o ponto de interceptação = %.4f " %(total_x))

for i in range(k):
    delta_y =(y-r_i) - (yirobo)
    total_y = delta_y *0.02 + y-r_i * t_desloc_min
print("Posição y do robo até o ponto de interceptação = %.4f" %(total_y))

