from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West SideStory"]
num_oscars = [5, 11, 3, 8, 10]
# barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 às
# coordenadas à esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(movies)]
# as barras do gráﬁco com as coordenadas x à esquerda [xs], alturas
[num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")
# nomeia o eixo x com nomes de ﬁlmes na barra central
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()