def make_car(fabricante, modelo, **kwargs):
    kwargs['fabricante'] = fabricante
    kwargs['modelo'] = modelo
    return kwargs

meu_carro = make_car(
        'Polo',
        'Volkswagen',
        cor='Prata',
        ano=2020,
        ar_condicionado=True,
)
print(meu_carro)
