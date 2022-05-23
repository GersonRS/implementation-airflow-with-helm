FROM customising_airflow:latest

ARG SPARK_VERSION="3.2.1"
ARG HADOOP_VERSION="3.2"
ARG openjdk_version="11"

###############################
## Begin JAVA installation
###############################

USER root
RUN mkdir -p /usr/share/man/man1/

RUN set -ex \
    && buildDeps=' \
            freetds-dev \
            libkrb5-dev \
            libsasl2-dev \
            libssl-dev \
            libffi-dev \
            libpq-dev \
            git \
        ' \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        freetds-bin \
        build-essential \
        default-libmysqlclient-dev \
        apt-utils \
        curl \
        rsync \
        netcat \
        locales \
        iputils-ping \
        telnet \
        wget \
    && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    "openjdk-${openjdk_version}-jre-headless" \
    ca-certificates-java && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

###############################
## SPARK files and variables
###############################

ENV SPARK_HOME /usr/local/spark

# Spark submit binaries and jars (Spark binaries must be the same version of spark cluster)
RUN cd "/tmp" && \
        wget --no-verbose "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
        tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
        mkdir -p "${SPARK_HOME}/bin" && \
        mkdir -p "${SPARK_HOME}/assembly/target/scala-2.12/jars" && \
        cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin/." "${SPARK_HOME}/bin/" && \
        cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/." "${SPARK_HOME}/assembly/target/scala-2.12/jars/" && \
        rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

# Create SPARK_HOME env var
RUN export SPARK_HOME
ENV PATH $PATH:$SPARK_HOME/bin

# Create JAVA_HOME env var
ENV JAVA_HOME /usr/lib/jvm/java-${openjdk_version}-openjdk-amd64

RUN export SPARK_HOME
ENV PATH $PATH:$SPARK_HOME/bin

###############################
## Airflow extra dependencies
###############################
# USER airflow
# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir apache-airflow-providers-apache-spark apache-airflow-providers-cncf-kubernetes pyspark pandas apache-airflow-providers-papermill ipykernel

###############################
## Copy custom dags
###############################

COPY ./dags /opt/airflow/dags