def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)


n = int(input('Digite um número positivo: '))
print(f'A soma de todos os números até {n} é {sum(n)}')
