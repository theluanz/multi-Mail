import csv

def existe(user):
    inc=0
    tmp = open('projeto/files/log.csv', 'r')
    leitor =csv.reader(tmp)
    for i in leitor:
        if(i[0]==user):
            inc+=1
    if inc==0:
        return True
    else:
        return False

def createLocal(user,passwd):
    if existe(user):
        data_list = [user, passwd],
        with open('projeto/files/log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_list)
            return True
    else:
        print("Usuario ja existe!")
        return False

def logar(user,passwd):
    inc=0
    tmp = open('projeto/files/log.csv', 'r')
    leitor =csv.reader(tmp)
    for i in leitor:
        if ((i[0]==user) and (i[1]==passwd)):
            inc+=1
    if inc==0:
        print("Usuario não existe ou senha incorreta!")
        return False
    else:
        print("Logado com sucesso!")
        return True
