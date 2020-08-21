if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    item = student_marks.get(query_name)
    longitud = len(item)
    suma = sum(item)
    resultado = suma/longitud
    print("{:.2f}".format(resultado))
