import matplotlib.pyplot as grafico
posx = []
posy =[]

for indice in open("xy_robo.txt","r"):
    indice = [i for i in indice.split()]
    posx.append(float(indice[0]))
    posy.append(float(indice[1]))

grafico.ylabel("Posição Y (m)")
grafico.xlabel("Posição X (m)")
grafico.axis(ymin = 0, ymax=7)
grafico.axis(xmin = 0, xmax = 7)
grafico.title("Trajetória da bola dentro do campo")

grafico.plot(posx,posy)
grafico.show()