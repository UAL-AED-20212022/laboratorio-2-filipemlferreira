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

def registar_nome_pais_num_determinado_index(lista_paises, nome_pais):
    lista_paises.insert_at_index(nome_pais)
    return lista_paises

def verificar_numero_elementos(lista_paises):
    return lista_paises.get_count()

def verificar_nome_pais(lista_paises, nome_pais):
    lista_paises.search_item(nome_pais)
    return nome_pais

def elimina_nome_inicio(lista_paises):
    pais_numero_um = lista_paises.start_node.item
    lista_paises.delete_at_start()
    return pais_numero_um
