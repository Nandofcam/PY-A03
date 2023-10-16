# [PY-A03] Considere o seguinte dicionário em Python:

pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}

# a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao:

idade_joao = 0

for pessoa in pessoas:
    if pessoa == "João":
        idade_joao = pessoas["João"]
    else:
        continue

print(idade_joao)

# b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31

pessoas["Ana"] = 31

print(pessoas)

# c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com maior idade:

maior_idade = 0
mais_velha = ''

for pessoa in pessoas:
    if pessoas[pessoa] > maior_idade:
        maior_idade = pessoas[pessoa]
        mais_velha = pessoa
    else:
        continue

print(f"A pessoa mais velha é {mais_velha} com {maior_idade} anos!")