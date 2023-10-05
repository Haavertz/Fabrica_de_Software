# Definir um dicionário com informações de alunos
alunos = {
    "João": 85,
    "Maria": 92,
    "Pedro": 78,
    "Ana": 88,
    "Carlos": 95
}

# Acessar valores
nota_maria = alunos["Maria"]
print(f"A nota da Maria é {nota_maria}.")

print("=-"*60)

# Adicionar um novo aluno e sua nota
alunos["Lúcia"] = 91
print(f"Adicionado aluno Lúcia com nota {alunos['Lúcia']}.")

print("=-"*60)

# Modificar a nota de um aluno
print(alunos)
alunos["Pedro"] = 80
print(f"A nota atualizada do Pedro é {alunos['Pedro']}.")
print(alunos)

print("=-"*60)

# Verificar se um aluno existe
if "Carlos" in alunos:
    print("Carlos está na lista de alunos.")

print("=-"*60)

# Remover um aluno
del alunos["Ana"]
print("Ana foi removida da lista de alunos.")

print("=-"*60)

# Listar todos os alunos e suas notas
print("Lista de alunos e notas:")
for aluno, nota in alunos.items():
    print(f"{aluno}: {nota}")

print("=-"*60)

# Obter o número de alunos
numero_alunos = len(alunos)
print(f"Número de alunos na lista: {numero_alunos}")


# Copiar o dicionário de alunos
copia_alunos = alunos.copy()

print("=-"*60)

# Limpar o dicionário de alunos
alunos.clear()
print("Dicionário de alunos limpo:", alunos)
