favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'rust',
        'phil':'python',
}
novas_pessoas = ['max', 'edward', 'anna', 'phil']
for p in novas_pessoas:
    if p in favorite_languages.keys():
        print(f'{p.title()} obrigado por responder a pesquisa.')
    else:
        print(f'Por favor, {p.title()} participe de nossa pesquisa.')
