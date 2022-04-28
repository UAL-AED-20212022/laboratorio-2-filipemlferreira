from models.LinkedList import LinkedList

def registar_nome_pais_inicio(lista_paises, nome_pais):
    lista_paises.insert_at_start(nome_pais)
    return lista_paises

def registar_nome_pais_fim(lista_paises, nome_pais):
    lista_paises.insert_at_end(nome_pais)
    return lista_paises

def registar_nome_pais_depois_outro_elemento(lista_paises, nome_pais, pais_registado):
    lista_paises.insert_after_item(pais_registado,nome_pais)
    return lista_paises

def registar_nome_pais_antes_outro_elemento(lista_paises, nome_pais, pais_registado):
    lista_paises.insert_before_item(pais_registado, nome_pais)
    return lista_paises

def registar_nome_pais_num_determinado_index(lista_paises, nome_pais, index):
    lista_paises.insert_at_index(int(index), nome_pais)
    return lista_paises

def verificar_numero_elementos(lista_paises):
    return lista_paises.get_count()

def verificar_nome_pais(lista_paises, nome_pais):
    if lista_paises.search_item(nome_pais) == True:
        return True
    else:
        return False

def elimina_nome_inicio(lista_paises):
    pais_numero_um = lista_paises.start_node.item
    lista_paises.delete_at_start()
    return pais_numero_um

def elimina_nome_fim(lista_paises):
    pais_fim = lista_paises.get_last_node()
    lista_paises.delete_at_end()
    return pais_fim

def eliminar_pais_especifico(lista_paises, pais_eliminado):
    if lista_paises.search_item(pais_eliminado) == True:
        lista_paises.delete_element_by_value(pais_eliminado)
        return True
    else:
        return False

