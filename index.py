import crypto
import login
print("Seja bem vindo ao multiMail SE")
loginOrNot = 0
userAccount=""
passAccount=""
rePassAccount=""

while loginOrNot==0:
    print("Esccolha uma das opções:")
    loginOrNot= int(input("0 - Cadastre-se\n1 - Login\n"))

    if loginOrNot == 1:
        userAccount=crypto.encrypt_string(str(input("Digite seu nome de usuário do Sistema\n")))
        passAccount=crypto.encrypt_string(str(input("Digite sua senha do Sistema\n")))
        login.logar(userAccount,passAccount)
    elif loginOrNot == 0:
        userAccount=crypto.encrypt_string(str(input("Digite seu nome de usuário do Sistema\n")))
        passAccount=crypto.encrypt_string(str(input("Digite sua senha do Sistema\n")))
        rePassAccount=crypto.encrypt_string(str(input("Digite sua senha do Sistema\n")))
        if passAccount==rePassAccount:
            loginOrNot=login.createLocal(userAccount, passAccount)
        else:
            print("As senhas não são iguais!")
            print(" \n"*4)
