def print_formatted(number):
    # your code goes here
    for item in range (number):
        print(item+1, end = '  ')
        print(oct(item+1)[2:], end = '  ')
        print(hex(item+1)[2:], end = '  ')
        print(bin(item+1)[2:])


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
