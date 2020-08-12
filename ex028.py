# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATROS ALUNOS
# PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE.
# LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno escolhido foi {}'.format(sorteio))




