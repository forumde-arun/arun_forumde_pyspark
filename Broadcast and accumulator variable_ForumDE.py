# Databricks notebook source
# DBTITLE 1,Broadcast Join
from pyspark.sql.functions import broadcast
# Create two DataFrames: one large and one small
large_df = spark.createDataFrame([(1, "Alice"), (2, "Bob"), (3, "Charlie")], ["id", "name"])
small_df = spark.createDataFrame([(1, "Sales"), (2, "Marketing")], ["id", "department"])

# Perform a broadcast join
joined_df = large_df.join(broadcast(small_df), "id", "inner")

# Show the joined DataFrame
joined_df.show()


# COMMAND ----------

# DBTITLE 1,Normal way of doing Join
from pyspark.sql.functions import broadcast
# Create two DataFrames: one large and one small
large_df = spark.createDataFrame([(1, "Alice"), (2, "Bob"), (3, "Charlie")], ["id", "name"])
small_df = spark.createDataFrame([(1, "Sales"), (2, "Marketing")], ["id", "department"])

# Perform a broadcast join
joined_df = large_df.join(small_df, "id", "inner")

# Show the joined DataFrame
joined_df.show()


# COMMAND ----------

# DBTITLE 1,Accumulator
# Create an accumulator for counting even numbers
even_count = sc.accumulator(0)

# Define a function to check if a number is even and update the accumulator
def check_even(number):
    global even_count
    if number % 2 == 0:
        even_count += 1

# Create an RDD with some numbers
numbers_rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Apply the function to each element in the RDD
numbers_rdd.foreach(check_even)

# Get the value of the accumulator
total_even_count = even_count.value

# Print the total count of even numbers
print("Total count of even numbers:", total_even_count)

# COMMAND ----------

# DBTITLE 1,Normal Way of Doing Counting
# Create an RDD
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Filter the even numbers
even_rdd = rdd.filter(lambda x: x % 2 == 0)

# Count the even numbers
count_even = even_rdd.count()

print("Total number of even numbers:", count_even)