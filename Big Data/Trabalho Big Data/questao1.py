from pyspark.sql import SparkSession

# Cria uma SparkSession
spark = SparkSession.builder.appName("ExemploLeituraCSV").getOrCreate()

# Lê o arquivo CSV

imdb_df = spark.read.csv('imdb-reviews-pt-br.csv', 
                         header=True, 
                         quote="\"", 
                         escape="\"", 
                         encoding="UTF-8")

def map1(x):
  # Esta função deve retornar uma tupla (sentiment, id).
  # o argumento de entrada x é uma linha do dataframe imdb_df 
  # com os dados em um formato semelhante à um dicionário
  # Apague a linha abaixo para iniciar seu código.
  pass

def reduceByKey1(x,y):
  # Coloque aqui o seu código para retornar o resultado necessário.
  # x e y são valores que serão somados, pois o reduceByKey receberá
  # apenas o segundo elemento da tupla vinda da saída da função map.
  # Apague a linha abaixo para iniciar seu código.
  pass

# Linha de código para aplicar o map/reduce no seu dataframe spark
resultado = imdb_df.rdd.map(map1).reduceByKey(reduceByKey1).collect()
# Coloque aqui o código para imprimir o resultado. Não esqueça seu RU:
print(resultado)

# Encerra a SparkSession
spark.stop()