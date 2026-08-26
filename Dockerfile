# Imagem base com JDK 8 (Jython 2.7.x roda bem sobre Java 8)
FROM openjdk:8-jdk-slim

LABEL maintainer="Atividade Jython - Interoperabilidade Python/Java"

ENV JYTHON_VERSION=2.7.3
ENV JYTHON_HOME=/opt/jython

# Instala o Jython automaticamente durante o build da imagem,
# para que o usuario NAO precise instalar nada manualmente na maquina.
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    wget -q -O /tmp/jython-installer.jar \
        "https://repo1.maven.org/maven2/org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" && \
    java -jar /tmp/jython-installer.jar -s -d ${JYTHON_HOME} && \
    rm -f /tmp/jython-installer.jar && \
    apt-get purge -y wget && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="${JYTHON_HOME}/bin:${PATH}"

WORKDIR /app
COPY . /app

# Ao rodar o container, executa os exemplos.
CMD ["bash", "-c", "\
    echo '===================================================' && \
    echo '  Exemplo 1: java.io (arquivos) + java.util (datas) ' && \
    echo '===================================================' && \
    jython exemplo1.py && \
    echo '' && \
    echo '===================================================' && \
    echo '  Exemplo 2: java.util (ArrayList, HashMap, TreeMap) ' && \
    echo '===================================================' && \
    jython exemplo2.py && \
    echo '' && \
"]
