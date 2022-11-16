dic={'daniel':'12997367523','califa':'12345678'}
print("seja bem vindo a minha lista de contato")
menu='v'
while menu != 's':
    menu=input("escolha sua opçaõ: V,C,E,S").upper()
    while menu!='T':
        menu = input("Escolha uma opção: V,C,E,S").upper()
        if menu =='V':
            print(dic)
        elif menu=='C':
            nome = input('adicionar um nome:')
            telefone= input("adicinar um telefone:")
            dic[nome]=telefone
        elif menu=='E':
            nome=input("dijite o nome do contato para ser excluido:")
            del dic[nome]
        else:
         print("ate logo")