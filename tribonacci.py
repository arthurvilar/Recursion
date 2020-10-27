def t(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return t(n-1) + t(n-2) + t(n-3)


def main():
    n = int(input('Num da sequência de tribonacci: '))
    print(f'O {n}° termo da sequência é {t(n)}')


if __name__ == '__main__':
    main()
