def mutate_string(string, position, character):
    lista = list(string)
    lista.insert(position,character)
    lista.pop(position+1)
    string=  ''.join(map(str, lista))
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
