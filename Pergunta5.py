# 5) Escreva um programa que inverta os caracteres de um string. 

# IMPORTANTE: 

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

# b) Evite usar funções prontas, como, por exemplo, reverse;

def Reverse(texto):
    aux = list(texto)
    mirror = []
    for i in range(len(aux)-1,-1,-1):
        mirror.append(aux[i])
    mirror = ''.join(mirror)
    return print("\nA string invertida é:", mirror,"\n")

string = input("\nDigite a string a ser invertida: ")

Reverse(string)