# Databricks notebook source
# MAGIC %md
# MAGIC ## Final Code for Cache and Persist

# COMMAND ----------

df_loan = spark.read.format("csv").options(header=True,inferSchema=True).load('dbfs:/databricks-datasets/lending-club-loan-stats/LoanStats_2018Q2.csv')

# COMMAND ----------

df_loan_filter=df_loan.filter(df_loan["loan_amnt"] > 2000)

# COMMAND ----------

df_loan_filter.count()

# COMMAND ----------

df_loan_filter.cache()

# COMMAND ----------

#Calculation1
# Groupby with DEPT along FEE with sum()
df_summed1=df_loan_filter.groupBy('home_ownership').sum('loan_amnt')

# COMMAND ----------

df_summed1.show()

# COMMAND ----------

#Calculation2
df_summed2=df_loan_filter.groupBy('verification_status').sum('loan_amnt')

# COMMAND ----------

df_summed2.show()