import re
def imprimir(resultado):

    if resultado:
        print (resultado)
    else:
        print(resultado)

if __name__ == '__main__':
    s = raw_input()

    alfa = re.findall('[a-zA-Z0-9_]',s)
    alfa = ''.join(alfa)
    imprimir(alfa.isalnum())

    letras = re.findall('[a-zA-Z_]',s)
    letras   = ''.join(letras)
    imprimir(letras.isalpha())

    numeros = re.findall('[0-9]',s)
    numeros= ''.join(numeros)
    imprimir(numeros.isdigit())

    lower= re.findall('[a-z]',s)
    lower= ''.join(lower)
    imprimir(lower.islower())

    upper= re.findall('[A-Z]',s)
    upper= ''.join(upper)
    imprimir(upper.isupper())


S = raw_input()
print True if any(k in "0123456789" or k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
print True if any(k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
print True if any(k in "0123456789" for k in S) else False
print True if any(k in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
print True if any(k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for k in S) else False


# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
print any(map(lambda x: x.isalnum(), s))
print any(map(lambda x: x.isalpha(), s))
print any(map(lambda x: x.isdigit(), s))
print any(map(lambda x: x.islower(), s))
print any(map(lambda x: x.isupper(), s))
