def reajuste(sal):
    if sal <= 1621:
        novo = sal + (sal * 0.15)
    else:
        novo = sal + (sal * 0.10)
    return novo
