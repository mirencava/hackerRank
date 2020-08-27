import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
#validar si el regex es correcto
if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            re.compile(input())
            is_valid = True
        except re.error:
            is_valid = False

        print (is_valid)
