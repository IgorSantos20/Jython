#!/bin/bash
set -e

echo "==================================================="
echo "  Exemplo 1: java.io (arquivos) + java.util (datas) "
echo "==================================================="
jython exemplo1.py

echo ""
echo "==================================================="
echo "  Exemplo 2: java.util (ArrayList, HashMap, TreeMap) "
echo "==================================================="
jython exemplo2.py

echo ""
echo "Obs: o exemplo3.py usa Java Swing (interface grafica) e deve"
echo "ser executado localmente com \"jython exemplo3.py\", pois requer"
echo "um ambiente grafico (nao roda em container headless)."
