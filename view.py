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