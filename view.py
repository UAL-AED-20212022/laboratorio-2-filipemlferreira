import controller
from models.LinkedList import LinkedList


lista_paises = LinkedList()


def main():
  
  while True:
    
    
    instrucao = input().split(" ")


    if instrucao[0] == "RPI":
      pais_novo = instrucao[1]
      RPI(lista_paises, pais_novo)

    if instrucao[0] == "RPF":
      pais_novo = instrucao[1]
      RPF(lista_paises, pais_novo)

    if instrucao[0] == "RPDE":
      pais_novo = instrucao[1]
      RPDE(lista_paises, pais_novo)

    if instrucao[0] == "RPAE":
      pais_novo = instrucao[1]
      RPDE(lista_paises, pais_novo)
    
    if instrucao[0] == "RPII":
      pais_novo = instrucao[1]
      RPII(lista_paises, pais_novo)

    if instrucao[0] == "VNE":
      VNE(lista_paises)
      print(f"O número de elementos são {len(lista_paises)}")
    
    if instrucao[0] == "VP":
      pais_novo = instrucao[1]
      if VP(lista_paises) == True:
        print(f"O país {pais_novo} encontra-se na lista.")
      else:
          print(f"O país {pais_novo} não se encontra na lista.")
    
    if instrucao[0] == "EPE":
      EPE(lista_paises)
      print(f"O país {EPE(lista_paises)} foi eliminado da lista.")
    
    if instrucao[0] == "EUE":
      EUE(lista_paises)
      print(f"O país {EUE(lista_paises)} foi eliminado da lista.")


    if instrucao[0] == "EP":
      pais_eliminado = instrucao[1]
      if EP(lista_paises) == True:
        print(f"O país {pais_eliminado} foi eliminado da lista.")
      else:
        print(f"O país {pais_eliminado} não se encontra na lista.")








def RPI(lista_paises, nome_pais):
  controller.registar_nome_pais_inicio(lista_paises, nome_pais)
  return lista_paises.traverse_list()


def RPF(lista_paises, nome_pais):
  controller.registar_nome_pais_fim(lista_paises, nome_pais)
  return lista_paises.traverse_list()

def RPDE(lista_paises, nome_pais):
  controller.registar_nome_pais_depois_outro_elemento(lista_paises, nome_pais)
  return lista_paises.traverse_list()

def RPAE(lista_paises, nome_pais):
  controller.registar_nome_pais_antes_outro_elemento(lista_paises,nome_pais)
  return lista_paises.traverse_list()

def RPII(lista_paises, nome_pais):
  controller.registar_nome_pais_num_determinado_index(lista_paises, nome_pais)
  return lista_paises.traverse_list()

def VNE(lista_paises):
  return controller.verificar_numero_elementos(lista_paises)

def VP(lista_paises, pais):
  if controller.verificar_nome_pais(lista_paises, pais) == True:
    return True
  else:
    return False

def EPE(lista_paises):  
  return controller.elimina_nome_inicio(lista_paises)

def EUE(lista_paises):
  return controller.elimina_nome_fim(lista_paises)

def EP(lista_paises, pais_eliminado):
  if controller.eliminar_pais_especifico(pais_eliminado, lista_paises) == True:
    return True
  else:
   return False

  
  
  