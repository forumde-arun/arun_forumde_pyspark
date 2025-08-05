# Databricks notebook source
# DBTITLE 1,Create Dataframe
# Step 1: Create sample DataFrame
data = [("arun",1), ("amit",2), ("anup",3)]
df = spark.createDataFrame(data, ["name","marks"])
df.show()

# COMMAND ----------

# DBTITLE 1,Create UDF in PySpark
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType


# Step 2: Define Python function
def square(x):
    return x * x

# Step 3: Convert it to a Spark UDF
square_udf = udf(square, IntegerType())

# Step 4: Use the UDF in withColumn
df = df.withColumn("squared", square_udf(df["marks"]))
df.show()


# COMMAND ----------

# Step 1: Create sample DataFrame
data = [("arun",1), ("amit",2), ("anup",3)]
df = spark.createDataFrame(data, ["name","marks"])
df.show()

# COMMAND ----------

# DBTITLE 1,Create UDF in Spark SQL
from pyspark.sql.types import IntegerType

# Step 1: Reuse the same SparkSession and DataFrame
df.createOrReplaceTempView("numbers")

# Step 2: Define a function
def double(x):
    return x * 2

# Step 3: Register it as a UDF
spark.udf.register("double_udf", double, IntegerType())

# Step 4: Use it in SQL
spark.sql("SELECT name,marks, double_udf(marks) AS doubled FROM numbers").show()
