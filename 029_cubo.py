num = list(n ** 3 for n in range(1, 11))
print('Os dez primeiros cubos são: ', end='')
for n in num:
    print(f'[{n}] ', end='')
    