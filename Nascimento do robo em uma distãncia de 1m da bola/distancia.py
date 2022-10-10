import math
linha = -1
posx = []
posy = []
bolay = []
bolax = []
robox = []
roboy =[]

for indice in open("trajetoria_bola_diurno.txt","r"):
    if linha == -1:
        pass
    else:
        indice = [i for i in indice.split()]
        posx.append(float(indice[1]))
        posy.append(float(indice[2]))
    linha += 1


def posicao():
    for i in range(linha):
            
        bolax.append(posx[i])
        bolay.append(posy[i])

    for i in range(linha):
        print("%.3f  %.3f" %(bolax[i], bolay[i]))

posicao()
#para achar a distancia entre o robo e a bolinha podemos usar a fórmula de distância entre dois pontos: