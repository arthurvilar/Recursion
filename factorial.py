def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def main():
    n = int(input('Digite o numero para calcular o fatorial: '))
    print(fact(n))


main()
