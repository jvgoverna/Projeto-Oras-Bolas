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

for i in range(linha):
    print("%.2f %.2f" %(velXbolinha[i], velYbolinha[i]))    # verificação se a velocidade está sendo calculada direito