'''2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser 
previamente definida no código;'''

def existeA(texto):
    texto = texto.lower()
    if "a" in texto:
        return True
    
    return False

def qtdA(texto):
    texto = texto.lower()
    count = 0

    for i in texto:
        if i == "a":
            count += 1

    return count

def main():
    entrada = input("Digite uma string: ")
    qtd_a = qtdA(entrada)
    if existeA(entrada):
        print(f'Existe "a" em sua string e o "a" aparece {qtd_a}')
    else:
        print('Não existe "a" na sua string')

if __name__ == '__main__':
    main()
