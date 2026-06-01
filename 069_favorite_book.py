def favorite_book(title):
    """Exibe uma mensagem mostrando meu livro favorito"""
    print(f'Um dos meus livros favoritos é {title.title()}')


livro = input('Qual seu livro favorito? ')
favorite_book(livro)
