print ("Bem-vindo ao clan do Bola de BG3")
nome = input("Digite seu nome:")
idade = input("digite sua idade:")
sexo = input("Digites seu sexo:")
nacionalidade = input("digite sua nacionalidade:")
classe = input("digite sua classe:")
raça = input("digite sua raça:")
try:
    nivel = int(input("digite seu nivel de 1 a 12:"))
except ValueError:
    print("Por favor, digite um número válido para o nível.")
    exit()

if nivel >= 5:
    print("parabéns, você foi aceito no clan")
else:
    print("obrigado pela inscrição")
print("nome:", nome)
print( "idade:", idade)
print("sexo:", sexo)
print("nacionalidade:", nacionalidade)
print("classe:",classe)
print("raça:", raça)
print("nivel:", nivel)