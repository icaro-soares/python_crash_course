def criar_personagem(nick, **kwargs):
    """Cria uma lista com o nome e estatísticas de um personagem"""
    kwargs['nick'] = nick
    return kwargs
