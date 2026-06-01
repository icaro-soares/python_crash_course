current_users = ['val', 'andre', 'bia', 'ana', 'icaro', 'JOHN']
new_users = ['sandra', 'ana', 'josé', 'val', 'bru', 'john']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for new in new_users:
    if new.lower() in current_users_lower:
        print(f'O usuário {new} já existe, por favor escolha outro.')
    else:
        print(f'Seja bem vindo(a), usuário {new}')
