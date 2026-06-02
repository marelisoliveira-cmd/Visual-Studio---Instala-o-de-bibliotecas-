import matplotlib.pyplot as plt

nomes = ["Ana", "Bruno", "Carlos", "Duda"]
notas = [8, 6, 9, 7]

plt.bar(nomes, notas)
plt.title("Teste da Biblioteca Matplotlib")
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.show()