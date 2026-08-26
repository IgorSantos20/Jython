# -*- coding: utf-8 -*-
"""
Exemplo 1 - Manipulacao de arquivos (java.io) e datas (java.util / java.text)
------------------------------------------------------------------------------
Este programa demonstra a interoperabilidade entre Python e Java atraves do
Jython. As classes File, FileWriter, BufferedWriter, FileReader e
BufferedReader (pacote java.io) sao importadas e usadas diretamente no
codigo Python, exatamente como seriam usadas em um programa Java. Tambem
usamos java.util.Date e java.text.SimpleDateFormat para gerar timestamps.

Nenhuma biblioteca Python de terceiros e usada: toda a manipulacao de
arquivos e datas e feita 100% com classes da API padrao do Java.
"""

from java.io import File, FileWriter, BufferedWriter, FileReader, BufferedReader
from java.util import Date
from java.text import SimpleDateFormat


def escrever_log(caminho, mensagens):
    """Escreve uma lista de mensagens em um arquivo, usando classes Java de I/O."""
    arquivo = File(caminho)                       # java.io.File
    writer = BufferedWriter(FileWriter(arquivo, True))  # java.io.FileWriter/BufferedWriter (append=True)

    formato = SimpleDateFormat("dd/MM/yyyy HH:mm:ss")   # java.text.SimpleDateFormat

    for msg in mensagens:
        agora = Date()  # java.util.Date -> data/hora atual fornecida pela JVM
        linha = "[%s] %s" % (formato.format(agora), msg)
        writer.write(linha)
        writer.newLine()
        print("Gravado -> %s" % linha)

    writer.close()
    return arquivo


def ler_log(caminho):
    """Le e imprime o conteudo do arquivo usando java.io.BufferedReader."""
    print("\n--- Conteudo do arquivo (%s) ---" % caminho)
    reader = BufferedReader(FileReader(File(caminho)))
    linha = reader.readLine()
    while linha is not None:
        print(linha)
        linha = reader.readLine()
    reader.close()


if __name__ == "__main__":
    caminho_log = "saida/log_atividade.txt"

    # Garante que o diretorio existe, usando java.io.File (nao os.mkdir do Python)
    pasta = File("saida")
    if not pasta.exists():
        pasta.mkdirs()
        print("Diretorio 'saida' criado via java.io.File")

    mensagens = [
        "Programa Jython iniciado.",
        "Testando integracao Python + Java.",
        "Gravando dados de exemplo em arquivo de texto.",
        "Fim da execucao do exemplo 1."
    ]

    arquivo_gerado = escrever_log(caminho_log, mensagens)

    # Metodos do proprio objeto Java File sendo chamados a partir do Python
    print("\nArquivo gerado em: %s" % arquivo_gerado.getAbsolutePath())
    print("Tamanho do arquivo: %d bytes" % arquivo_gerado.length())

    ler_log(caminho_log)
