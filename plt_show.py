import matplotlib.pyplot as plt

x = [1, 2, 4, 4, 5]
y = [2, 3, 7, 1, 0]
# x2 = [2, 4, 6, 8, 10]
# y2 = [5, 1, 5, 7, 4]
titulo = "Gráico de barras"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixo_x)
plt.ylabel(eixo_y)

# Gráfico de barras
# plt.bar(x, y, label="Grupo 1")
# plt.bar(x2, y2, label="Grupo 2")

# Gráfico de scatter
plt.plot(x, y, color="red", linestyle="-")
plt.scatter(x, y, label="Meus pontos", color="r", marker="*", s=100)

plt.legend()
plt.show()
