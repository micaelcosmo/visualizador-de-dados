import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
titulo = "Gráico de barras"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixo_x)
plt.ylabel(eixo_y)
# plt.plot(x, y)
# Gráfico de barras
plt.bar(x, y)
plt.show()
