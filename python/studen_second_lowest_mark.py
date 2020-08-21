if __name__ == '__main__':
    student_tuples=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_tuples.append([name,score])


    student_tuples = sorted(student_tuples, key=lambda score: score[1])
    student_min = min(student_tuples, key=lambda score: score[1])
    index = student_tuples.index(student_min)
    nota_mas_baja = student_tuples[index]

    lista_final = [item for item in student_tuples if item[1] != nota_mas_baja[1]]
    segunda_mas_baja = lista_final[0]
    lista_final = [item for item in lista_final if item[1] == segunda_mas_baja[1] ]
    lista_final = sorted(lista_final, key=lambda name: name[0])
    for item in lista_final:
        print (item[0])
