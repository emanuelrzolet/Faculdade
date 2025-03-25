import os
import requests
import zipfile
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, sum, split, size

# Identificador pessoal (RU)
RU = 4557826
contador4557826 =0
meu_identificador_4557826= "Emanuel Rosa Zolet"

# Obtenção e descompactação dos dados
endereco_web = "https://raw.githubusercontent.com/N-CPUninter/Big_Data/main/data/imdb-reviews-pt-br.zip"
nome_arquivo_zip = "imdb-reviews-pt-br.zip"

resposta_http = requests.get(endereco_web, stream=True)

if resposta_http.status_code == 200:
    with open(nome_arquivo_zip, "wb") as arquivo_local:
        for segmento in resposta_http.iter_content(1024):
            arquivo_local.write(segmento)
    print(f"Download de {nome_arquivo_zip} finalizado!")
else:
    print(f"Falha no download do arquivo: {resposta_http.status_code}")

with zipfile.ZipFile(nome_arquivo_zip, 'r') as arquivo_zip:
    arquivo_zip.extractall()
    print(f"Conteúdo de {nome_arquivo_zip} extraído.")

os.remove(nome_arquivo_zip)
print(f"{nome_arquivo_zip} removido.")

# Configuração da sessão Spark
nome_app_spark = "Análise de Reviews IMDB com PySpark"
modo_mestre = "local[*]"  # Utiliza todos os cores disponíveis

print("Inicializando sessão Spark...")
sessao_spark_ativa: SparkSession = SparkSession.builder.appName(nome_app_spark).master(modo_mestre).getOrCreate()
print("Sessão Spark operacional! ")

# Definição do esquema e leitura dos dados
estrutura_dados = StructType([
    StructField("id", IntegerType(), True), #mudança de tipo para int
    StructField("text_en", StringType(), True),
    StructField("text_pt", StringType(), True),
    StructField("sentiment", StringType(), True),
])

reviews_imdb: DataFrame = sessao_spark_ativa.read.csv('imdb-reviews-pt-br.csv',
                                    header=True,
                                    quote="\"",
                                    escape="\"",
                                    encoding="UTF-8",
                                    schema=estrutura_dados) #aplicação do schema na leitura

# Funções para análise dos dados
def filtrar_reviews_negativas(dados: DataFrame) -> DataFrame:
    return dados.filter(col("sentiment") == "neg")

def calcular_soma_ids_negativos(reviews: DataFrame) -> DataFrame:
    return reviews.select(sum("id").alias("soma_ids_negativos"))

def calcular_contagem_palavras(dados: DataFrame) -> DataFrame:
    return dados.select(
        col("sentiment"),
        size(split(col("text_en"), "\\s+")).alias("palavras_ingles"),
        size(split(col("text_pt"), "\\s+")).alias("palavras_portugues"),
    )

def agrupar_contagem_por_sentimento(contagem_palavras: DataFrame) -> DataFrame:
    return contagem_palavras.groupBy("sentiment").agg(
        sum("palavras_ingles").alias("total_palavras_ingles"),
        sum("palavras_portugues").alias("total_palavras_portugues"),
    )

# Execução da análise
reviews_negativas = filtrar_reviews_negativas(reviews_imdb)
resultado_soma_ids = calcular_soma_ids_negativos(reviews_negativas).collect()[0][0]
print("Resposta questão 1 - Emanuel Rosa Zolet - RU: 4557826")
print(f"Soma dos IDs das reviews negativas: {resultado_soma_ids}")

# Questão 2
contagem_palavras_df = calcular_contagem_palavras(reviews_negativas)
resultado_contagem = agrupar_contagem_por_sentimento(contagem_palavras_df).collect()[0]
diferenca_palavras = resultado_contagem[2] - resultado_contagem[1]

print("Resposta questão 2, Emanuel Rosa Zolet - RU: 4557826")
print(f"Diferença na contagem de palavras (Português - Inglês): {diferenca_palavras}")