unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []
while unconfirmed_users:
    confirmed = unconfirmed_users.pop()
    print(f'Verificando usuário: {confirmed.title()}')
    confirmed_users.append(confirmed)
print('\nUsuarios confirmados:')
for confirmed in sorted(confirmed_users):
    print(f'\t{confirmed.title()}')
