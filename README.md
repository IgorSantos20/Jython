# Atividade Jython — Interoperabilidade entre Python e Java

Projeto desenvolvido para explorar o **Jython**, uma implementação da
linguagem Python que executa sobre a **JVM (Java Virtual Machine)**,
permitindo utilizar diretamente classes e bibliotecas Java dentro de
programas escritos em Python.

---

## 1. O que é o Jython?

O **Jython** é uma implementação da linguagem Python 2 escrita em Java e
executada sobre a JVM. Diferente do CPython (implementação "padrão" do
Python, escrita em C), o Jython compila o código Python em **bytecode
Java**, que roda diretamente na máquina virtual Java.

Isso traz uma vantagem importante: como o Jython roda sobre a JVM, ele
consegue **importar e usar diretamente qualquer classe Java** disponível no
classpath — bibliotecas padrão (`java.io`, `java.util`, `javax.swing`,
`java.net`, etc.) ou até bibliotecas de terceiros — sem necessidade de
wrappers, bindings especiais ou serialização de dados entre processos. Do
ponto de vista do programador, um `import java.util.ArrayList` dentro de um
arquivo `.py` funciona de forma muito parecida com um `import` de um módulo
Python nativo.

Em resumo: o Jython permite **misturar a sintaxe simples e dinâmica do
Python com todo o ecossistema de bibliotecas do Java**, porque ambos passam
a compartilhar a mesma plataforma de execução (a JVM).

> Observação: o Jython implementa a linguagem **Python 2**, não Python 3.
> Por isso, os exemplos deste projeto usam sintaxe compatível com Python 2
> (ex.: `print "algo"` funciona, mas aqui usamos `print(...)` com
> parênteses, que também é válido em Python 2 quando aplicado a um único
> argumento).

---

## 2. Programas desenvolvidos

O repositório contém três programas Python executados com Jython. Todos
demonstram, de forma explícita, o uso de classes Java dentro do código
Python.

### `exemplo1.py` — Manipulação de arquivos (`java.io`) + datas (`java.util` / `java.text`)

- Cria (se necessário) um diretório usando `java.io.File`.
- Escreve um arquivo de log (`saida/log_atividade.txt`) usando
  `java.io.FileWriter` e `java.io.BufferedWriter`.
- Gera um timestamp para cada linha do log usando `java.util.Date` e
  formata a data com `java.text.SimpleDateFormat`.
- Lê o arquivo de volta usando `java.io.FileReader` e
  `java.io.BufferedReader`.
- Consulta metadados do arquivo (caminho absoluto, tamanho em bytes) usando
  métodos do próprio objeto `java.io.File`.

### `exemplo2.py` — Estruturas de dados (`java.util`)

- Cria e manipula uma `java.util.ArrayList` (equivalente Java de uma lista).
- Ordena e inverte a lista usando os métodos estáticos
  `java.util.Collections.sort()` e `java.util.Collections.reverse()`.
- Itera sobre a `ArrayList` usando o `for item in lista:` "pythonico" do
  Python — o Jython permite iterar em Python sobre qualquer objeto Java que
  implemente `java.lang.Iterable`.
- Cria uma `java.util.HashMap` e uma `java.util.TreeMap` (que ordena
  automaticamente pelas chaves), demonstrando o uso de mapas Java a partir
  de Python.

### `exemplo3.py` (bônus) — Interface gráfica com Java Swing

- Cria uma janela gráfica usando `javax.swing.JFrame`, `JButton`, `JLabel`
  e `JPanel`, além de `java.awt.FlowLayout` e `java.awt.BorderLayout` para
  o layout.
- Implementa a interface Java `java.awt.event.ActionListener` **dentro de
  uma classe Python**, mostrando como uma classe Python pode "herdar" e
  implementar uma interface Java nativamente.
- Exibe uma caixa de diálogo Java (`javax.swing.JOptionPane`) ao fechar o
  programa.

> Este exemplo abre uma janela e por isso **precisa de ambiente gráfico**.
> Não roda dentro do container Docker por padrão (headless). Veja a seção
> "Executando o `exemplo3.py`" mais abaixo para instruções de como rodá-lo.

---

## 3. Classes e bibliotecas Java utilizadas

| Pacote Java              | Classes utilizadas                                                        | Onde é usado |
|---------------------------|----------------------------------------------------------------------------|--------------|
| `java.io`                 | `File`, `FileWriter`, `BufferedWriter`, `FileReader`, `BufferedReader`      | `exemplo1.py` |
| `java.util`               | `Date`, `ArrayList`, `HashMap`, `TreeMap`, `Collections`                    | `exemplo1.py`, `exemplo2.py` |
| `java.text`               | `SimpleDateFormat`                                                          | `exemplo1.py` |
| `javax.swing`             | `JFrame`, `JButton`, `JLabel`, `JPanel`, `JOptionPane`                      | `exemplo3.py` |
| `java.awt`                | `FlowLayout`, `BorderLayout`                                                | `exemplo3.py` |
| `java.awt.event`          | `ActionListener`                                                            | `exemplo3.py` |

---

## 4. Como Python e Java estão sendo integrados

A integração acontece porque o **Jython compila o código Python para
bytecode que roda na JVM**, a mesma máquina virtual usada para executar
programas Java. Como consequência prática:

1. **Imports diretos**: qualquer classe Java disponível no classpath pode
   ser importada em Python exatamente como um módulo, por exemplo:
   ```python
   from java.io import File
   from java.util import ArrayList
   ```
2. **Instanciação e chamada de métodos**: objetos Java são criados e
   manipulados com sintaxe Python normal (`File("saida")`,
   `lista.add("Maria")`, `writer.close()`), mas por baixo são instâncias
   Java de verdade, com todos os seus métodos originais disponíveis.
3. **Implementação de interfaces Java em Python**: no `exemplo3.py`, a
   classe Python `AcaoBotao` estende `ActionListener` (uma interface
   Java) e implementa o método `actionPerformed`, que é chamado
   automaticamente pela JVM quando o botão Swing é clicado.
4. **Recursos "pythonicos" sobre objetos Java**: estruturas Java que
   implementam `Iterable` (como `ArrayList`) podem ser percorridas com o
   `for x in y:` do Python, e `Collections` (uma classe utilitária Java)
   é chamada como se fosse uma função de biblioteca padrão.

Ou seja: não há tradução, serialização, chamadas de rede ou processos
separados entre "o lado Python" e "o lado Java" — é **um único programa,
rodando em um único processo (a JVM)**, apenas escrito com a sintaxe do
Python.

---

## 5. Estrutura do repositório

```
atividade-jython/
├── README.md
├── Dockerfile
├── exemplo1.py      # java.io + java.util.Date + java.text
├── exemplo2.py      # java.util (ArrayList, HashMap, TreeMap, Collections)
└── saida/           # pasta onde exemplo1.py grava o arquivo de log
```

---

## 6. Como executar o projeto (instalando o Jython localmente)

### Pré-requisitos

- Java JDK instalado (versão 8 ou superior) — necessário porque o Jython
  roda sobre a JVM.
- Jython instalado na máquina.

### Passo a passo

1. **Baixar e instalar o Jython** (caso ainda não tenha):
   - Baixe o instalador em: https://www.jython.org/download
   - Execute o instalador:
     ```bash
     java -jar jython-installer-2.7.3.jar
     ```
   - Siga o assistente (pode escolher instalação padrão) e adicione a
     pasta `bin` do Jython ao `PATH` do sistema.

2. **Verificar a instalação**:
   ```bash
   jython --version
   ```

3. **Clonar este repositório**:
   ```bash
   git clone <URL-DO-SEU-REPOSITORIO>
   cd atividade-jython
   ```

4. **Executar os exemplos**:
   ```bash
   jython exemplo1.py
   jython exemplo2.py
   ```

5. Após rodar `exemplo1.py`, o arquivo gerado pode ser conferido em:
   ```
   saida/log_atividade.txt
   ```

---

## 7. Como executar o projeto utilizando Docker

Não é necessário instalar Java ou Jython na máquina — o `Dockerfile` já
instala tudo automaticamente durante o build da imagem.

### Build da imagem

```bash
docker build -t atividade-jython .
```

### Executar os exemplos (1 e 2)

```bash
docker run --rm atividade-jython
```

Isso executa automaticamente `exemplo1.py` e `exemplo2.py` dentro do
container e imprime a saída no terminal.

---

## 8. Vídeo de apresentação

O vídeo explicando o projeto e demonstrando a integração Python + Java
(máx. 5 minutos, rosto visível) está disponível em:

> _(cole aqui o link do Loom ou anexe o vídeo neste repositório)_

---

## 9. Autor

Atividade desenvolvida como exercício prático sobre interoperabilidade
entre linguagens em uma mesma plataforma de execução (JVM), utilizando o
Jython como ponte entre Python e Java.
