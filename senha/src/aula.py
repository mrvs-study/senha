
"""Construa um programa em Python que realize o cadastramento de três alunos,
digitando nome , primeiranota e segundanota. Como saída mostre a média dos alunos, e os
os alunos aprovados ( nota maior ou igual que 7), em recuperação (nota maior ou igual que
4 e menor que 6.9) e reprovado ( nota menor que 3.9"""
media =0

for aula in range(3):
    aluno = input ("digite seu nome: ")
    nota1 =float (input ("digite sua nota1: "))
    nota2 =float (input ("digite sua nota2: "))
    media = (nota1+nota2) / 2
    print(media)
    if media>=7:
     print("aluno "+aluno+" esta de aprovado")
    elif media>=4:
     print("aluno "+aluno+" esta de recuperacão")
    else :
     print("aluno "+ aluno+ " reprovado")