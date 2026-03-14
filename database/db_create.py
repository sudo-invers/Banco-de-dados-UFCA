from configparser import ConfigParser

def configuracao(filename='./db.ini', section='criacao'):
    """ Criacao do banco de dadps do postgres

    Args:
        filename (str, optional): Localizacao do arquivo de inicializacao.
        section (str, optional): A secao utilizada do arquivo de inicializacao que sera lido.

    Returns:
        _type_: Um dicionario, contendo os dados do database criado.
    """
    parser = ConfigParser
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db [param[0]] = param[1]
    else:
        raise Exception("Secao {0} não encontrado no arquivo {1}".format(section, filename))
    return db