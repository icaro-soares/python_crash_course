def make_album(artist, album_title, songs=None):
    """Mostra as informações sobre um álbum de música"""
    album = {'artist':artist, 'album':album_title}
    if songs:
        album['songs'] = songs
    return album

print(make_album('Evanescence', 'The Open Door', 13))
print(make_album('Shaman', 'Fairytail'))
print(make_album('Iron Maiden', 'Fear of the Dark'))
