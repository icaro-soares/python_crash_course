def make_album(artist, album_title,):
    """Retorna as informações de um álbum"""
    album = {'artist':artist, 'título':album_title}
    return album

while True:
    artista = input('Artista do álbum: ').strip().capitalize()
    if artista in 'Qq':
        break
    nome_album = input('Nome do Álbum: ').strip().capitalize()
    if nome_album in 'Qq':
        break
    album = make_album(artista, nome_album)
    print(album)
    print('-=' * 30)
    