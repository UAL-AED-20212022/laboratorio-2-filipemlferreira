from models.LinkedList import LinkedList

def registar_nome_pais_inicio(lista_paises, nome_pais):
    lista_paises.insert_at_start(nome_pais)
    return lista_paises

def registar_nome_pais_fim(lista_paises, nome_pais):
    lista_paises.insert_at_end(nome_pais)
    return lista_paises

def registar_nome_pais_depois_outro_elemento(lista_paises, nome_pais):
    lista_paises.insert_after_item(nome_pais)
    return lista_paises

def registar_nome_pais_antes_outro_elemento(lista_paises, nome_pais):
    lista_paises.insert_before_item(nome_pais)
    return lista_paises
