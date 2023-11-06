def nome():
    aluno=input("Digite seu nome: ")
    return aluno
pp=nome()

def soma_media():
   nota1=float (input("digite sua 1 nota: "))
   
   nota2=float (input("digite sua 2 nota: "))
   
   soma = (nota1+nota2)/2
   return soma

media_aluno = soma_media()

print("A media do aluno",pp,"é:",media_aluno)