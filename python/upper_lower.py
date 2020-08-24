def swap_case(s):
    cadena = s.split()
    resultado = ""
    for item in s:
        if item.islower():

            resultado= resultado +  item.upper()
        elif item.isupper():
            item.lower()
            resultado= resultado + item.lower()
        else:
            resultado = resultado + item

    return resultado

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
