
# sequencia = [10, 20, 30, 40, 50]: Aqui, criamos uma lista chamada sequencia que contém cinco valores inteiros.

# for indice, valor in enumerate(sequencia):: Esta linha inicia um loop for que percorrerá os elementos da lista sequencia usando a função enumerate. A função enumerate é usada para obter tanto o índice quanto o valor de cada elemento na sequência.

# print(f"Índice: {indice}, Valor: {valor}"): Dentro do loop for, imprimimos o índice e o valor de cada elemento. Usamos uma f-string (format string) para formatar a saída de maneira legível. A variável indice conterá o índice do elemento atual e valor conterá o valor do elemento atual.

# Então, quando o código é executado, ele percorre a lista sequencia, e para cada elemento, ele exibe o índice e o valor correspondentes na tela. Isso produzirá a seguinte saída:

# Índice: 0, Valor: 10
# Índice: 1, Valor: 20
# Índice: 2, Valor: 30
# Índice: 3, Valor: 40
# Índice: 4, Valor: 50
# O loop for com enumerate é uma maneira conveniente de percorrer uma sequência enquanto rastreia os índices e valores de cada elemento.

sequencia = [10, 20, 30, 40, 50]

for indice, valor in enumerate(sequencia):
    print(f"Índice: {indice}, Valor: {valor}")