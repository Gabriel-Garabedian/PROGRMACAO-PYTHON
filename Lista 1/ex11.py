#Crie um sistema de login que não permite que o nome de usuário e a senha sejam iguais. 

nome= input("Digite o nome de usuário: ")
senha= input("Digite a senha: ")

if nome == senha:
    print("Nome de usuário e senha não podem ser iguais.")

else:
    print("Cadastro realizado com sucesso")