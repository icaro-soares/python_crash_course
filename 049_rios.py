rios = {
        'amazonas':'brasil',
        'reno':'frança',
        'nilo':'egito',
}
for rio, país in rios.items():
    print(f'O rio {rio.title()} passa pelo {país.title()}')
for rio in rios.keys():
    print(f'Rio {rio.title()}')
for país in rios.values():
    print(f'País {país.title()}')
