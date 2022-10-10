import math
linha = -1
posx = []
posy = []
bolay = []
bolax = []

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

robox = uniform(0 , 2)
roboy = uniform(0 , 1.5)
print("X do Robo: %.2f" % (robox))
print("Y do Robo: %.2f" % (roboy))
