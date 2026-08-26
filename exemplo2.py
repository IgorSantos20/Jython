# -*- coding: utf-8 -*-
"""
Exemplo 2 - Estruturas de dados de java.util manipuladas a partir de Python (Jython)
-------------------------------------------------------------------------------------
Este programa demonstra o uso de colecoes Java (ArrayList, HashMap, TreeMap) e
de metodos utilitarios estaticos (Collections.sort, Collections.reverse)
diretamente a partir de codigo Python, incluindo iteracao "pythonica" (for-in)
sobre objetos que sao, na verdade, instancias de classes Java.
"""

from java.util import ArrayList, HashMap, Collections, TreeMap


def demo_arraylist():
    print("=== java.util.ArrayList ===")
    lista = ArrayList()  # cria uma ArrayList Java, nao uma lista Python
    for nome in ["Maria", "Joao", "Ana", "Carlos", "Beatriz"]:
        lista.add(nome)  # metodo .add() da API Java

    print("Lista original (Java ArrayList): %s" % lista)

    Collections.sort(lista)  # metodo estatico Java para ordenar a colecao
    print("Lista ordenada com Collections.sort(): %s" % lista)

    Collections.reverse(lista)  # metodo estatico Java para inverter a colecao
    print("Lista invertida com Collections.reverse(): %s" % lista)

    # O Jython permite iterar com o "for x in y" do Python sobre um objeto Java
    # que implementa java.lang.Iterable, como a ArrayList.
    print("Iterando com for-in do Python sobre um objeto Java:")
    for item in lista:
        print(" - %s" % item)

    return lista


def demo_hashmap():
    print("\n=== java.util.HashMap / java.util.TreeMap ===")
    idades = HashMap()  # HashMap Java (sem ordem garantida)
    idades.put("Maria", 28)
    idades.put("Joao", 34)
    idades.put("Ana", 22)

    print("HashMap (ordem nao garantida): %s" % idades)

    # TreeMap ordena automaticamente as chaves - recebe um HashMap no construtor
    ordenado = TreeMap(idades)
    print("TreeMap (ordenado por chave): %s" % ordenado)

    for chave in ordenado.keySet():  # keySet() retorna um Set Java, iteravel em Python
        valor = ordenado.get(chave)
        print(" - %s tem %d anos" % (chave, valor))


if __name__ == "__main__":
    demo_arraylist()
    demo_hashmap()
